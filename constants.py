# =============================================================================
# constants.py
# Shared constants, file extension sets, and table column definitions.
# =============================================================================

# -- Authentication -----------------------------------------------------------
# Demo password for authorized image viewing.
# Change before deployment -- in production this should be hashed and stored securely.
DEMO_PASSWORD = "wilco2025"

# -- Ollama -------------------------------------------------------------------
OLLAMA_URL      = "http://localhost:11434/api/generate"
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL    = "llama3"
OLLAMA_LLAVA    = "llava-llama3"

# -- File extensions ----------------------------------------------------------
IMG_EXTS = frozenset({".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".tif", ".heic", ".heif"})
VID_EXTS = frozenset({".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".webm", ".m4v"})

# -- Results table column definitions: (field_name, header_label, width_px) --
IMAGE_PREVIEW_COLS = [
    ("_thumb",               "Preview",      72),   # special-cased thumbnail column
    ("id",                   "ID",           40),
    ("filename",             "Filename",    160),
    ("ext",                  "Type",         45),
    ("bytes",                "Size (B)",     75),
    ("width",                "W",            50),
    ("height",               "H",            50),
    ("aspect_ratio",         "Ratio",        55),
    ("avg_brightness",       "Bright.",      65),
    ("avg_contrast",         "Contrast",     65),
    ("dominant_color_1",     "Color 1",      62),
    ("dominant_color_2",     "Color 2",      62),
    ("dominant_color_3",     "Color 3",      62),
    ("hist_bhattacharyya",   "Bhatt. Dist.", 85),
    ("detected_objects",     "Objects",     180),
    ("detection_confidence", "Conf.",        140),
    ("bucket_phash",         "pHash Grp",    70),
    ("bucket_dbscan",        "DBSCAN Grp",   75),
    ("exif_datetime",        "Date Taken",  130),
    ("exif_camera_make",     "Camera Make",  95),
    ("exif_camera_model",    "Camera Model",110),
    ("exif_gps_lat",         "GPS Lat",      85),
    ("exif_gps_lon",         "GPS Lon",      85),
    ("exif_gps_link",        "Maps Link",   300),
]

VIDEO_PREVIEW_COLS = [
    ("video_pair_1",          "Video 1",      140),
    ("video_pair_2",          "Video 2",      140),
    ("frame_id",              "Frame",         50),
    ("timestamp",             "Time (s)",      65),
    ("similarity_ssim",       "SSIM %",        65),
    ("similarity_mse",        "MSE",           65),
    ("similarity_psnr",       "PSNR (dB)",     75),
    ("motion_score",          "Motion",        65),
    ("detected_objects",      "Objects",      180),
    ("detection_confidence",  "Conf.",         140),
]

SINGLE_VIDEO_COLS = [
    ("frame_id",              "Frame",         50),
    ("timestamp",             "Time (s)",      70),
    ("motion_score",          "Motion",        70),
    ("avg_brightness",        "Brightness",    80),
    ("avg_contrast",          "Contrast",      70),
    ("dominant_color_1",      "Color 1",       65),
    ("dominant_color_2",      "Color 2",       65),
    ("dominant_color_3",      "Color 3",       65),
    ("detected_objects",      "Objects",      200),
    ("detection_confidence",  "Conf.",         150),
]

# -- Column help text (right-click any header to see this) --------------------
COLUMN_HELP = {
    "_thumb": (
        "Preview",
        "A thumbnail of the image. Blurred by default to protect sensitive content. "
        "Click 'Authorize Access' and enter the investigator password to unlock full previews. "
        "Double-click any row to open a larger preview popup."
    ),
    "id": (
        "ID",
        "A sequential number assigned to each file during analysis. "
        "Used to identify and reference individual items in reports and exports."
    ),
    "filename": (
        "Filename",
        "The original name of the file as it exists on disk. "
        "No files are ever renamed or modified by this tool."
    ),
    "ext": (
        "Type",
        "The file extension, indicating the image format (e.g. .jpg, .png, .bmp). "
        "Different formats use different compression methods which can affect analysis results."
    ),
    "bytes": (
        "Size (B)",
        "The file size in bytes. Unusually small files may indicate heavy compression or cropping. "
        "Two visually identical images with very different file sizes may have been processed differently."
    ),
    "width": (
        "Width (px)",
        "The horizontal resolution of the image in pixels."
    ),
    "height": (
        "Height (px)",
        "The vertical resolution of the image in pixels."
    ),
    "aspect_ratio": (
        "Aspect Ratio",
        "The proportional relationship between width and height, expressed as W:H. "
        "Common ratios include 4:3 (older cameras), 16:9 (widescreen), and 1:1 (square). "
        "An unusual ratio may indicate the image has been cropped."
    ),
    "avg_brightness": (
        "Brightness",
        "The average pixel brightness across the entire image, on a scale from 0 (pure black) "
        "to 255 (pure white). Very dark images (below ~50) may be intentionally obscured. "
        "Very bright images (above ~200) may be overexposed."
    ),
    "avg_contrast": (
        "Contrast",
        "The standard deviation of pixel brightness values. A higher number means the image "
        "contains a wider range of light and dark areas. A very low contrast score may indicate "
        "a washed-out, foggy, or heavily filtered image."
    ),
    "dominant_color_1": (
        "Dominant Color 1",
        "The most prevalent color in the image, identified using K-means clustering. "
        "Displayed as a hex color code (e.g. #3A2F1C) with a color swatch in the preview strip. "
        "Useful for grouping images by scene or environment."
    ),
    "dominant_color_2": (
        "Dominant Color 2",
        "The second most prevalent color in the image. "
        "Together with Color 1 and Color 3, these three colors represent the overall "
        "color palette of the image."
    ),
    "dominant_color_3": (
        "Dominant Color 3",
        "The third most prevalent color in the image. "
        "Comparing dominant colors across a group of images can help confirm they were "
        "taken in the same environment or under similar lighting conditions."
    ),
    "hist_bhattacharyya": (
        "Bhattacharyya Distance",
        "A measure of how similar the color distributions are between images in the same "
        "pHash similarity group. Calculated using color histograms across all three color channels. "
        "A score of 0.0 means the color distributions are identical. "
        "Higher scores indicate greater color difference. "
        "Only computed for images that share a pHash group -- single images will show 0."
    ),
    "detected_objects": (
        "Detected Objects",
        "Objects identified in the image by the YOLO AI detection model. "
        "YOLO (You Only Look Once) is a computer vision system that draws bounding boxes "
        "around recognized objects and labels them. Only available when AI detection is enabled "
        "before running the analysis. Common detections include person, car, phone, backpack, etc."
    ),
    "detection_confidence": (
        "Detection Confidence",
        "The confidence score (0.0 to 1.0) for each detected object, indicating how certain "
        "the YOLO model is about its identification. A score of 0.90 means 90% confidence. "
        "Scores below the minimum threshold set before analysis are filtered out automatically."
    ),
    "bucket_phash": (
        "pHash Group",
        "The similarity group this image was assigned to using perceptual hashing (pHash). "
        "pHash generates a fingerprint of the image based on its visual structure. "
        "Images with fingerprints within a set distance of each other are placed in the same group. "
        "Images that share a group number are visually similar. "
        "Yellow rows in the table indicate images that belong to a group with at least one other image. "
        "The threshold for grouping can be adjusted before running the analysis -- "
        "lower values are stricter."
    ),
    "exif_datetime": (
        "Date Taken",
        "The date and time the photo was captured, extracted from the EXIF metadata "
        "embedded in the image file by the camera or device. "
        "Format is typically YYYY:MM:DD HH:MM:SS. "
        "This timestamp is set by the device at capture time and is separate from "
        "the file system modification date, making it more reliable as evidence. "
        "Empty if the image has no EXIF data or was stripped of metadata."
    ),
    "exif_camera_make": (
        "Camera Make",
        "The manufacturer of the device that captured the image, as recorded in EXIF metadata. "
        "Examples: Apple, Samsung, Canon, SONY. "
        "Can help identify the type of device used and corroborate other evidence. "
        "Empty if not present in the file."
    ),
    "exif_camera_model": (
        "Camera Model",
        "The specific model of the device that captured the image, as recorded in EXIF metadata. "
        "Examples: iPhone 14 Pro, SM-G991B, Canon EOS R6. "
        "Combined with the make, this can narrow down the exact device used. "
        "Empty if not present in the file."
    ),
    "exif_gps_lat": (
        "GPS Latitude",
        "The latitude coordinate where the image was captured, extracted from GPS data "
        "embedded in the EXIF metadata. Expressed in decimal degrees (e.g. 30.123456). "
        "Positive values are North, negative values are South. "
        "GPS coordinates in a photo can place a suspect or victim at a specific location "
        "at a specific time, making this one of the most forensically significant data points. "
        "Many devices embed GPS data by default unless location services are disabled. "
        "Empty if no GPS data is present."
    ),
    "exif_gps_lon": (
        "GPS Longitude",
        "The longitude coordinate where the image was captured. "
        "Expressed in decimal degrees (e.g. -97.654321). "
        "Positive values are East, negative values are West. "
        "See GPS Latitude for investigative significance. "
        "Empty if no GPS data is present."
    ),
    "exif_gps_link": (
        "Maps Link",
        "A Google Maps link generated from the GPS coordinates embedded in the image. "
        "Copy and paste this URL into a browser to see exactly where the photo was taken. "
        "Only present when both latitude and longitude are available in the EXIF data."
    ),
    "bucket_dbscan": (
        "DBSCAN Group",
        "A second-pass similarity grouping using DBSCAN (Density-Based Spatial Clustering). "
        "Unlike pHash which compares images one-to-one, DBSCAN looks at the entire dataset "
        "at once and finds natural clusters based on combined aHash and dHash feature vectors. "
        "A value of -1 means the image was classified as unique -- no close neighbors were found. "
        "DBSCAN can catch similarity patterns that pHash misses."
    ),
    "video_pair_1": (
        "Video 1",
        "The filename of the first video in a comparison pair. "
        "In Videos (folder) mode, every video in the folder is compared against every other video."
    ),
    "video_pair_2": (
        "Video 2",
        "The filename of the second video in a comparison pair."
    ),
    "frame_id": (
        "Frame",
        "The sequential index of the sampled frame within the video. "
        "Frames are sampled at a regular interval set before analysis (default every 0.5 seconds)."
    ),
    "timestamp": (
        "Timestamp",
        "The position in the video (in seconds) where this frame was sampled. "
        "Use this to locate the exact moment in the original video file."
    ),
    "similarity_ssim": (
        "SSIM (Structural Similarity)",
        "A measure of how visually similar two video frames are, expressed as a percentage. "
        "100% means the frames are structurally identical. 0% means completely different. "
        "SSIM accounts for luminance, contrast, and structure -- making it more sensitive "
        "than simple pixel comparison. Scores above 90% suggest near-duplicate footage."
    ),
    "similarity_mse": (
        "MSE (Mean Squared Error)",
        "The average squared difference between corresponding pixels in two frames. "
        "Lower values mean the frames are more similar at the pixel level. "
        "A score of 0.0 means the frames are pixel-perfect identical. "
        "Unlike SSIM, MSE does not account for perceptual structure -- "
        "a slight brightness shift can produce a high MSE even if the frames look the same."
    ),
    "similarity_psnr": (
        "PSNR (Peak Signal-to-Noise Ratio)",
        "A logarithmic measure of frame similarity expressed in decibels (dB). "
        "100 dB means the frames are identical. Above 50 dB indicates a near-exact copy. "
        "Values between 30-50 dB suggest moderate similarity. "
        "Below 30 dB indicates significant visual differences between the frames."
    ),
    "motion_score": (
        "Motion Score",
        "A measure of visual activity within a single frame, calculated by comparing "
        "the frame against a blurred version of itself. Higher scores indicate more edges, "
        "movement blur, or scene complexity. Lower scores suggest a static or near-static scene. "
        "Sudden spikes in motion score across sequential frames can indicate a scene change "
        "or significant event in the footage."
    ),
}