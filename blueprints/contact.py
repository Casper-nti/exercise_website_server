from flask import Blueprint, render_template, request, redirect, url_for
from blueprints.data.about_entry import about_entries

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")



@contact_bp.route("/cms/about_manager/create", methods=["POST"])
def add_content():
    # Extract data from the form
    print(request.form)
    title = request.form["heading"]
    imageFilename = request.form["imageFilename"]
    introText = request.form["introText"]
    additionalInfo = request.form["additionalInfo"]
    isActive = "isActive" in request.form 
