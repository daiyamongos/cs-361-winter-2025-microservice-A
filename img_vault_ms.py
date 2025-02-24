# Image Vault Microservice
# A microservice that receives images and stores them in a locally stored folder, also retrieves, and deletes them through HTTP (communication pipe).
# by Louie Baobao

from flask import Flask, jsonify, request, send_file
import mimetypes
import os

app = Flask(__name__)

LOCAL_STORAGE = "img_vault"
os.makedirs(LOCAL_STORAGE, exist_ok=True)

# store uploaded images
@app.route("/upload", methods=["POST"])
def upload_img():
    if "file" not in request.files:
        return jsonify({"message": "no image file uploaded"}), 400
    
    file = request.files["file"]
    img_name = file.filename

    if img_name.lower().endswith(".webp"):
        return jsonify({"message": "WEBP format is not supported"}), 400

    file.save(os.path.join(LOCAL_STORAGE, img_name)) 
    
    return jsonify({"message": f"image: \"{img_name}\" uploaded successfully", "img_name": img_name}), 201

# retrieve images
@app.route("/images/<img_name>", methods=["GET"])
def retrieve_img(img_name):
    image_path = os.path.join(LOCAL_STORAGE, img_name)

    print(f"Checking image path: {image_path}") # debug
    if not os.path.exists(image_path):
        return jsonify({"message": "image file not found!"}), 404
    
    mimetype = mimetypes.guess_type(image_path)[0] or "application/octet-stream"
    print(f"Mimetype: {mimetype}") # debug
    return send_file(image_path, mimetype=mimetype)

# delete images
@app.route("/images/<img_name>", methods=["DELETE"])
def delete_img(img_name):
    image_path = os.path.join(LOCAL_STORAGE, img_name)

    if not os.path.exists(image_path):
        return jsonify({"message": "image not found!"}), 404

    os.remove(image_path)
    return jsonify({"message": f"image: \"{img_name}\" deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)