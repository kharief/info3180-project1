"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory

'''from django import forms'''
from .forms import PropertyForm

from werkzeug.utils import secure_filename
from app.models import Property
from app.forms import PropertyForm





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Danielle Blair")


@app.route('/properties/create', methods=['POST', 'GET'])
def create():
    """displaying the form to add a new property."""
    pform = PropertyForm()

    if pform.validate_on_submit():

        p_title = pform.title.data
        p_description = pform.description.data
        p_numrooms = pform.numrooms.data
        p_numbathrooms = pform.numbathrooms.data
        p_price = pform.price.data
        p_propertytype = pform.propertytype.data
        p_location = pform.location.data

        pimg = pform.propertypic.data
        filename = secure_filename(pimg.filename)
        pimg.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        property = Property(title=p_title, description=p_description, numrooms=p_numrooms,
                            numbathrooms=p_numbathrooms,price= p_price, propertytype= p_propertytype,
                            location= p_location, filename=filename)
        db.session.add(property)
        db.session.commit()

        flash('Property Created and Saved', 'success')
        return redirect(url_for('get_properties')) 

    return render_template('create.html', form=pform)

@app.route('/properties')
def get_properties():
    """displaying a list of all properties in the database"""
    properties=db.session.query(Property).all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<propertyid>')
def aboutproperty(propertyid):
    """For viewing an individual property by the specific property id"""
    property = db.session.query(Property).filter(Property.id == propertyid).first()
    return render_template('aboutproperty.html', property = property)

@app.route('/uploads/<filename>')
def get_images(filename):
    root = os.getcwd()
    return send_from_directory(root+'/'+app.config['UPLOAD_FOLDER'], filename)


def get_uploaded_images():
    import os
    rootdir = os.getcwd()
    fileslst = []
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            fileslst.append(file)
    return fileslst

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
