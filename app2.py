from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import get_user_by_username, get_user_by_id
from flask import abort
import Grade7PageConfig 
from LearnMappings import Grade3Mapper as mapper
import traceback

app = Flask(__name__)
app.secret_key = 'your-secret-key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Flask-Login requires this
@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

@app.route('/')
#@login_required
def index():
    return render_template('HomePage.html')
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@app.route('/LoginPage', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('LoginPage.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/Primary_Grade_3_Mathematics')
#@login_required
def primary3():
    grade_concept_rank = {}

    if current_user.is_authenticated:
        username = current_user.username
        #grade_concept_rank = GetConceptRank(3, username)

    return render_template('Primary_Grade_3.html')#, grade_concept_rank="ninja-rank")

@app.route('/Primary_Grade_4_Mathematics')
#@login_required
def primary4():
    grade_concept_rank = {}

    if current_user.is_authenticated:
        username = current_user.username
        #grade_concept_rank = GetConceptRank(4, username)

    return render_template('Primary_Grade_4.html')#, grade_concept_rank="ninja-rank")

@app.route('/Primary_Grade_5_Mathematics')
#@login_required
def primary5():
    grade_concept_rank = {}

    if current_user.is_authenticated:
        username = current_user.username
        #grade_concept_rank = GetConceptRank(5, username)

    return render_template('Primary_Grade_5.html')#, grade_concept_rank="ninja-rank")@app.route('/Primary_Grade_4_Mathematics')
@app.route('/Primary_Grade_6_Mathematics')
#@login_required ncomment this
def primary6():
    grade_concept_rank = {}

    if current_user.is_authenticated:
        username = current_user.username
        #grade_concept_rank = GetConceptRank(6, username) #figire this out w db

    return render_template('Primary_Grade_6.html')#, grade_concept_rank="ninja-rank") #uncomment this


@app.route('/Secondary-1-Grade-7-Mathematics')
def secondary1():
    page_name = request.args.get('pageName')
    ajax_bot_param = request.args.get('_escaped_fragment_')

    if ajax_bot_param:
        # Handle Googlebot requests
        try:
            html_page_name = Grade7PageConfig.PageMapping7A[ajax_bot_param]
            page_number = Grade7PageConfig.Grade7APages.index(html_page_name)
        except KeyError:
            try:
                html_page_name = Grade7PageConfig.PageMapping7B[ajax_bot_param]
                page_number = Grade7PageConfig.Grade7BPages.index(html_page_name)
            except KeyError:
                return f"Unknown AJAX fragment: {ajax_bot_param}", 404

        # Confirm the file exists (debugging tip)
        try:
            return render_template(html_page_name, page_number=page_number)
        except:
            return f"Template not found: {html_page_name}", 500

    else:
        # Normal user request
        params = {}
        if page_name:
            params['pageRedirectName'] = page_name

        try:
            return render_template('Grade-7/Grade-7.html', pageRedirectName='QuadraticEquations')
        except:
            return "Template not found: Grade-7/Grade-7.html", 500


@app.route('/Learn/Primary-Grade-3/<topic>/<subtopic>')
def primary3_handler1(topic, subtopic):
    try:
        fn, data = mapper.getMapping(subtopic, topic=topic)

        # Remove leading '/' and GroupTitle prefix if present
        fn_clean = fn.strip("/")
        if fn_clean.startswith(data["GroupTitle"] + "/"):
            fn_clean = fn_clean[len(data["GroupTitle"]) + 1:]  # +1 for slash

        filename = "Notes/Primary3/{}/{}".format(data["GroupTitle"], fn_clean)

        print("Rendering:", filename)  # Debug print

        return render_template(filename, **data)
    except KeyError:
        abort(404)
    except Exception as e:
        import traceback
        traceback.print_exc()
        abort(500)


@app.route('/Learn/Primary-Grade-3/<subtopic>')
def primary3_handler2(subtopic):
    try:
        fn, data = mapper.getMapping(subtopic)
        filename = "Notes/Primary3" + fn
        return render_template(filename, **data)
    except KeyError:
        abort(404)

@app.route('/Learn/Primary-Grade-4/<topic>/<subtopic>')
def primary4_handler1(topic, subtopic):
    try:
        fn, data = mapper.getMapping(subtopic, topic=topic)

        # Clean the filename
        fn_clean = fn.strip("/")
        if fn_clean.startswith("Learn/"):
            fn_clean = fn_clean[len("Learn/"):]
        fn_clean=fn_clean.replace("Primary-Grade-4","Primary4")
        filename = "Notes/{}".format(fn_clean)

        print("Rendering:", filename)  # Debug print

        return render_template(filename, **data)
    except KeyError:
        abort(404)
    except Exception as e:
        import traceback
        traceback.print_exc()
        abort(500)


@app.route('/Learn/Primary-Grade-4/<subtopic>')
def primary4_handler2(subtopic):
    try:
        fn, data = mapper.getMapping(subtopic)
        filename = "Notes/Primary4" + fn
        return render_template(filename, **data)
    except KeyError:
        abort(404)

@app.route('/Learn/Primary-Grade-5/<topic>/<subtopic>')
def primary5_handler1(topic, subtopic):
    try:
        fn, data = mapper.getMapping(subtopic, topic=topic)

        # Clean the filename
        fn_clean = fn.strip("/")
        if fn_clean.startswith("Learn/"):
            fn_clean = fn_clean[len("Learn/"):]
        fn_clean=fn_clean.replace("Primary-Grade-5","Primary5")
        filename = "Notes/{}".format(fn_clean)

        print("Rendering:", filename)  # Debug print

        return render_template(filename, **data)
    except KeyError:
        abort(404)
    except Exception as e:
        import traceback
        traceback.print_exc()
        abort(500)



@app.route('/Learn/Primary-Grade-5/<subtopic>')
def primary5_handler2(subtopic):
    try:
        fn, data = mapper.getMapping(subtopic)
        filename = "Notes/Primary5" + fn
        return render_template(filename, **data)
    except KeyError:
        abort(404)

@app.route('/Learn/Primary-Grade-6/<topic>/<subtopic>')
def primary6_handler1(topic, subtopic):
    try:
        fn, data = mapper.getMapping(subtopic, topic=topic)

        # Clean the filename
        fn_clean = fn.strip("/")
        if fn_clean.startswith("Learn/"):
            fn_clean = fn_clean[len("Learn/"):]
        fn_clean=fn_clean.replace("Primary-Grade-6","Primary6")
        filename = "Notes/{}.html".format(fn_clean)

        print("Rendering:", filename)  # Debug print

        return render_template(filename, **data)
    except KeyError:
        abort(404)
    except Exception as e:
        import traceback
        traceback.print_exc()
        abort(500)

@app.route('/Learn/Primary-Grade-6/<subtopic>')
def primary6_handler2(subtopic):
    try:
        fn, data = mapper.getMapping(subtopic)
        filename = "Notes/Primary6" + fn
        return render_template(filename, **data)
    except KeyError:
        abort(404)


@app.route('/learn')
def learn_page():
    return render_template('LearnPage.html', section='content')

if __name__ == '__main__':
    app.run(debug=True)
