import email_validator
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from models import User, Vehicle, Reservation
from flask_login import login_user, current_user, logout_user, login_required
from forms import RegistrationForm, LoginForm, ContactForm
from flask_mail import Message, Mail

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(nome=form.username.data, email=form.email.data, senha=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('A conta foi criada com sucesso.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login não foi bem sucedido. Por favor revê o email e password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    marcas = [v.marca for v in Vehicle.query.with_entities(Vehicle.marca).distinct()]
    modelos = [v.modelo for v in Vehicle.query.with_entities(Vehicle.modelo).distinct()]
    categorias = [v.categoria for v in Vehicle.query.with_entities(Vehicle.categoria).distinct()]
    tipos = [v.tipo for v in Vehicle.query.with_entities(Vehicle.tipo).distinct()]

    vehicles = None
    if request.method == 'POST':
        marca = request.form.get('marca')
        modelo = request.form.get('modelo')
        categoria = request.form.get('categoria')
        tipo = request.form.get('tipo')
        valor_diaria = request.form.get('valor_diaria')
        capacidade = request.form.get('capacidade')

        query = Vehicle.query

        if marca:
            query = query.filter(Vehicle.marca.ilike(f"%{marca}%"))
        if modelo:
            query = query.filter(Vehicle.modelo.ilike(f"%{modelo}%"))
        if categoria:
            query = query.filter(Vehicle.categoria.ilike(f"%{categoria}%"))
        if tipo:
            query = query.filter(Vehicle.tipo.ilike(f"%{tipo}%"))
        if valor_diaria:
            query = query.filter(Vehicle.valor_diaria <= float(valor_diaria))
        if capacidade:
            query = query.filter(Vehicle.capacidade >= int(capacidade))

        vehicles = query.all()

    return render_template('search.html', marcas=marcas, modelos=modelos, categorias=categorias, tipos=tipos, vehicles=vehicles)

@app.route("/location")
def location():
    return render_template('location.html', title='Localização')

@app.route("/about")
def about():
    return render_template('about.html', title='Sobre nós')


# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use o servidor SMTP do seu provedor de email
app.config['MAIL_PORT'] = 587  # Use a porta adequada para o seu servidor SMTP
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email' # Seu endereço de email
app.config['MAIL_PASSWORD'] = 'yourpass'  # Sua senha de email
mail = Mail(app)


# Rota para a página de contato
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(form.subject.data,
                      sender=form.email.data,
                      recipients=['mnanar27@gmail.com'])
        msg.body = f"""
        Nome: {form.name.data}
        Email: {form.email.data}
        Telemóvel: {form.phone.data}

        Mensagem:
        {form.message.data}
        """
        #mail.send(msg)
        flash('A tua mensagem foi enviada com sucesso.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form)
