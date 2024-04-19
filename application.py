from flask import Flask, render_template, redirect
import json
import urllib.request

app = Flask(__name__)

images = None

gameobjects = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 30, 31, 32, 33, 36, 39, 40, 41, 42, 43, 45, 47, 48, 49, 51, 52, 53, 56, 58, 60, 63, 70, 90, 91, 92, 95, 100, 105, 107, 112, 113, 114, 119, 124, 130, 131, 132, 133, 134, 137, 138, 139, 148, 150, 151, 153, 154, 155, 156, 159, 161, 163, 164, 166, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 498, 499, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 538, 558, 559, 560, 561, 562, 563, 564, 565, 566, 581, 601, 602, 603, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683,
]

def load_data():
    with urllib.request.urlopen("https://geo-tp.github.io/Model-Viewer/static/images.json") as url:
        return json.load(url)

def check_maintenance():
    try:
        with urllib.request.urlopen("https://displayidbrowser.mindphlux.net/maintenance") as url:
            return True
    except:
        return False

@app.route('/')
def portal():
    if not check_maintenance():
        return render_template('portal.html')
    else:
        return render_template('maintenance.html')

@app.route('/items')
def show_dirs():
    if not check_maintenance():
        dirs = []

        for image in images:
            if image['path'] not in dirs:
                dirs.append(image['path'])

        dirs.sort()
        return render_template('index.html', dirs=dirs)
    else:
        return render_template('maintenance.html')
    
@app.route('/go')
def show_gameobjects():
    if not check_maintenance():
        formatted_gameobjects = [{"display_id": go} for go in gameobjects]
        return render_template('go.html', gameobjects=formatted_gameobjects)
    else:
        return render_template('maintenance.html')

@app.route("/<string:dir>")
def show_dir(dir):
    if not check_maintenance():
        images_in_dir = []
        dirs = []

        for image in images:
            if image['path'] not in dirs:
                dirs.append(image['path'])
            if image['path'] == dir:
                images_in_dir.append(image)

        dirs.sort()
        return render_template('dir.html', images=images_in_dir, dir=dir, dirs=dirs)
    else:
        return render_template('maintenance.html')

@app.route("/api/usedby/<string:displayid>")
def get_used_by(displayid):

    for image in images:
        if image['id'] == int(displayid):
            return json.dumps(image['used_by'])

    return []

@app.route("/update")
def update():
    images = load_data()
    return redirect("/")

if __name__ == '__main__':
    images = load_data()
    from waitress import serve
    serve(app, host='0.0.0.0', port=8091)
