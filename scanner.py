#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import beginners_method_solve_visual, reduce_moves  
import cv2 
import numpy as np
from collections import OrderedDict

# --- UI constants ------------------------------------------------------------

WINDOW_NAME = "Rubik's Cube Scanner"
COLOR_KEYS = OrderedDict([
    ('w', 'W'), ('y', 'Y'), ('g', 'G'),
    ('b', 'B'), ('r', 'R'), ('o', 'O')
])

FACE_ORDER = ['F', 'R', 'B', 'L', 'U', 'D']  # capture order

# --- Text helpers ------------------------------------------------------------

def put_text(img, text, org, scale=0.6, color=(255,255,255), thickness=1):
    cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness, cv2.LINE_AA)

def draw_panel(img, x, y, w, h, alpha=0.35, fill=(0,0,0)):
    overlay = img.copy()
    cv2.rectangle(overlay, (x,y), (x+w, y+h), fill, -1)
    cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, img)

# --- Geometry: centered 3×3 square grid -------------------------------------

def compute_grid(frame_w, frame_h, cell_frac=0.14, gap_frac=0.06):
    base = min(frame_w, frame_h)
    cell = int(base * cell_frac)
    gap  = int(cell * gap_frac)
    grid_w = 3*cell + 2*gap
    grid_h = grid_w  # square

    gx = (frame_w - grid_w)//2
    gy = (frame_h - grid_h)//2

    rects = []
    for r in range(3):
        for c in range(3):
            x = gx + c*(cell+gap)
            y = gy + r*(cell+gap)
            rects.append((x, y, cell, cell))
    return (gx, gy, grid_w, grid_h), rects, cell, gap

# --- Sampling & classification -----------------------------------------------

def mean_hsv_in_rect(frame, rect, inset_ratio=0.28):
    x, y, w, h = rect
    dx = int(w*inset_ratio)
    dy = int(h*inset_ratio)
    roi = frame[y+dy:y+h-dy, x+dx:x+w-dx]
    if roi.size == 0:
        return None, None
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    m = hsv.reshape(-1,3).mean(axis=0)
    m = (float(m[0]), float(m[1]), float(m[2]))
    bgr = roi.reshape(-1,3).mean(axis=0)
    bgr = (int(bgr[0]), int(bgr[1]), int(bgr[2]))
    return m, bgr

def hue_dist(h1, h2):
    d = abs(h1 - h2)
    return min(d, 180 - d)

def nearest_calibrated_color(calib_hsv, hsv):
    if not calib_hsv or hsv is None:
        return '?'
    h, s, v = hsv
    best = None
    best_d = 1e9
    for letter, (ch, cs, cv) in calib_hsv.items():
        hd = hue_dist(h, ch)
        sd = abs(s - cs) / 255.0
        vd = abs(v - cv) / 255.0
        hdn = hd / 90.0
        d = 1.8*hdn + 1.2*sd + 0.8*vd
        if d < best_d:
            best_d = d
            best = letter
    return best if best is not None else '?'

# --- Drawing overlays ---------------------------------------------------------

def draw_grid_overlay(frame, rects, previews_bgr=None, preds=None, show_measured=True):
    for i, (x,y,w,h) in enumerate(rects):
        if previews_bgr is not None and show_measured:
            color = previews_bgr[i]
            cv2.rectangle(frame, (x,y), (x+w,y+h), color, -1)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (32,32,32), 2)
        else:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255), 2)

        if preds is not None:
            letter = preds[i]
            tx, ty = x + w//2 - 8, y + h//2 + 8
            put_text(frame, letter, (tx, ty), scale=1.0, color=(0,0,0), thickness=4)
            put_text(frame, letter, (tx, ty), scale=1.0, color=(255,255,255), thickness=1)

def draw_calibration_swatches(frame, calib_hsv, x=16, y=10, box=22):
    gap = 8
    total_w = len(COLOR_KEYS) * (box + gap) + 8
    draw_panel(frame, x-6, y-6, total_w, box+18, alpha=0.35)
    for i, (k, letter) in enumerate(COLOR_KEYS.items()):
        hsv = calib_hsv.get(letter, None)
        if hsv is None:
            color = (64, 64, 64)
            label = letter
        else:
            bgr = cv2.cvtColor(np.uint8([[[hsv[0], hsv[1], hsv[2]]]]),
                               cv2.COLOR_HSV2BGR)[0,0]
            color = (int(bgr[0]), int(bgr[1]), int(bgr[2]))
            label = letter
        px = x + i * (box + gap)
        cv2.rectangle(frame, (px, y), (px + box, y + box), (0,0,0), -1)
        cv2.rectangle(frame, (px+2, y+2), (px + box-2, y + box-2), color, -1)
        put_text(frame, label, (px+3, y + box + 14),
                 scale=0.5, color=(0,0,0), thickness=4)
        put_text(frame, label, (px+3, y + box + 14),
                 scale=0.5, color=(255,255,255), thickness=1)
    put_text(frame, "Calibrate: press w y g b r o on solid colors",
             (x, y + box + 34), scale=0.55, color=(255,255,255), thickness=1)

def draw_progress_panel(frame, faces_done, current_face):
    H, W = frame.shape[:2]
    panel_w, panel_h = 180, 150
    x = W - panel_w - 12
    y = 12
    draw_panel(frame, x, y, panel_w, panel_h, alpha=0.35)
    put_text(frame, "Capture Order:", (x+10, y+22))
    line_y = y + 48
    for f in FACE_ORDER:
        status = "✓" if f in faces_done else ("→" if f == current_face else "·")
        put_text(frame, f"{status} {f}", (x+14, line_y))
        line_y += 22

def draw_bottom_instructions(frame, calibrated_ok, current_face):
    H, W = frame.shape[:2]
    text = ("SPACE: capture  |  BACKSPACE: undo  |  v: toggle preview  |  ESC: quit"
            if calibrated_ok else
            "Point at one *solid color* and press: w y g b r o  (collect all 6)")
    (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
    pad = 12
    panel_w = min(W-20, tw + 2*pad)
    panel_h = th + 2*pad
    x = (W - panel_w)//2
    y = H - panel_h - 10
    draw_panel(frame, x, y, panel_w, panel_h, alpha=0.35)
    put_text(frame, text, (x+pad, y+panel_h - pad - 2))

# --- Main scanning loop -------------------------------------------------------

def scan_cube_and_solve(run_solver=False):
    """
    Returns:
      - if run_solver=False: cube dict {'F','R','B','L','U','D': [9 letters]}
      - if run_solver=True: (final_cube_dict, reduced_moves_list)
    """
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Cannot open camera (index 0).")

    calib_hsv = {}
    faces = {}
    face_idx = 0
    show_measured = True

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        H, W = frame.shape[:2]
        (_, _, _, _), rects, _, _ = compute_grid(W, H)

        # Live sampling & prediction
        previews_bgr, preds = [], []
        for rect in rects:
            hsv, bgr = mean_hsv_in_rect(frame, rect)
            previews_bgr.append(bgr if bgr is not None else (30,30,30))
            preds.append(nearest_calibrated_color(calib_hsv, hsv))

        # Overlays
        draw_grid_overlay(frame, rects, previews_bgr=previews_bgr,
                          preds=preds, show_measured=show_measured)
        draw_calibration_swatches(frame, calib_hsv, x=16, y=10, box=22)
        calibrated_ok = len(calib_hsv) == 6
        current_face = FACE_ORDER[face_idx] if face_idx < len(FACE_ORDER) else '-'
        draw_progress_panel(frame, faces_done=faces.keys(), current_face=current_face)
        draw_bottom_instructions(frame, calibrated_ok, current_face)

        cv2.imshow(WINDOW_NAME, frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC
            break

        # Calibration
        if key in [ord(k) for k in COLOR_KEYS.keys()]:
            if rects:
                mid_idx = 4
                hsv, _ = mean_hsv_in_rect(frame, rects[mid_idx], inset_ratio=0.10)
                if hsv is not None:
                    letter = COLOR_KEYS[chr(key)]
                    calib_hsv[letter] = hsv
                    print(f"Calibrated {letter}: HSV≈({int(hsv[0])},{int(hsv[1])},{int(hsv[2])})")

        # Toggle preview fill
        if key in (ord('v'), ord('V')):
            show_measured = not show_measured

        # Undo last face
        if key in (8, 127):  # BACKSPACE or DELETE
            if face_idx > 0:
                face_idx -= 1
                f = FACE_ORDER[face_idx]
                faces.pop(f, None)
                print(f"Undid face {f} ({face_idx+1}/{len(FACE_ORDER)})")

        # Capture face
        if key == 32:  # SPACE
            if not calibrated_ok:
                print("Finish calibration first (w,y,g,b,r,o).")
            else:
                face = FACE_ORDER[face_idx]
                captured = preds[:]  # 9 letters
                if '?' in captured:
                    print("Warning: some squares not confidently recognized ('?').")
                faces[face] = captured
                print(f"Captured {face}: {captured}")
                face_idx += 1
                if face_idx >= len(FACE_ORDER):
                    print("All faces captured.")
                    break

    cap.release()
    cv2.destroyAllWindows()

    # Validate
    if len(calib_hsv) != 6:
        missing = set(COLOR_KEYS.values()) - set(calib_hsv.keys())
        raise RuntimeError(f"Calibration incomplete, missing: {missing}")
    if len(faces) != 6:
        raise RuntimeError(f"Capture incomplete, got {len(faces)}/6 faces.")

    # Build cube
    cube = {f: faces[f] for f in FACE_ORDER}
    print("\nCube (FACE: 9 letters):")
    for f in FACE_ORDER:
        print(f"{f}: {cube[f]}")

    # Optionally solve
    if run_solver:
        print("\nSolving...")
        try:
            final_cube, moves = beginners_method_solve_visual(cube)  # returns (final_cube, move_log)
        except Exception as e:
            print(f"Solver call failed (adjust import/module): {e}")
            return cube  # fall back
        else:
            # If your move_log contains only moves, this is unnecessary; otherwise filter:
            valid = {"U","D","L","R","F","B","X","Y","Z"}
            moves = [m for m in moves if m and m[0] in valid]

            print("\nRaw moves:")
            print(' '.join(moves))

            reduced = reduce_moves(moves)
            print("\nReduced moves:")
            print(' '.join(reduced))

            return final_cube, reduced

    return cube

# --- Entry point -------------------------------------------------------------

if __name__ == "__main__":
    print("Calibration: point the camera at *one solid color* and press its key:")
    print("  w=White  y=Yellow  g=Green  b=Blue  r=Red  o=Orange")
    print("Collect all 6. Then press SPACE to capture each face in order:", FACE_ORDER)
    print("Keys: SPACE=capture  BACKSPACE=undo  v=toggle preview  ESC=quit\n")
    result = scan_cube_and_solve(run_solver=True)

