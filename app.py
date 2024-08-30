import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from pickletools import uint8
from re import I
import bcrypt
import pickle

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'mysecretkey')  # Required for session management

# Load MySQL configuration from environment variables with defaults
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'flaskapp')

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['username'] = username  # Store username in session
            return render_template('insert.html')
        else:
            return 'Invalid credentials!'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username')  # Retrieve username from session
    if not username:
        return redirect(url_for('login'))  # Redirect to login if not logged in
    return render_template('dashboard.html', username=session.get('username'))

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def result():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            nm=request.form['nm']
            app=request.form['app']
            el=request.form['el']
            mg=request.form['mg']
            ml=request.form['ml']
            time=request.form['time']
            nvi=request.form['nvi']
            nbi=request.form['nbi']
            nwp=request.form['nwp']
            aci=request.form['aci']
            acp=request.form['acp']
            acv=request.form['acv']
            pcsl=request.form['pcsl']
            if (pcsl=="0"):
                p_csl=0
            if (pcsl=="2.5"):
                p_csl=2.5
            if (pcsl=="5"):
                p_csl=5
            gender=request.form['g']
            if (gender=='M'):
                gn=1
            if (gender=='F'):
                gn=0
            heq=request.form['eq']
            if (heq=='jd'):
                eql=1
            if (heq=='hs'):
                eql=2
            if (heq=='coll'):
                eql=3
            if (heq=='mas'):
                eql=4
            if (heq=='assc'):
                eql=5
            if (heq=='md'):
                eql=6
            if (heq=='phd'):
                eql=7
            ins=request.form['ins']
            if (ins=='td'):
                insvr=1
            if (ins=='md'):
                insvr=2
            if (ins=='majd'):
                insvr=3
            if (ins=='tl'):
                insvr=4
            pd=request.form['pd']
            if (pd=='Y'):
                prd=1
            if (pd=='N'):
                prd=0
            pr=request.form['pr']
            if (pr=="1"):
                polr=1
            if (pr=="0"):
                polr=0
            occu=request.form['occu']
            if (occu=='af'):
                armedforces=1           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='cr'):
                armedforces=0           
                craftrepair=1           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='em'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=1        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='ff'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=1        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='hc'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=1      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='moi'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=1      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='os'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=1          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='phs'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=1        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='ps'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=1         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='prs'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=1        
                sales=0                  
                techsupport=0           
                transportmoving=0
            if (occu=='s'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=1                  
                techsupport=0           
                transportmoving=0
            if (occu=='ts'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=1           
                transportmoving=0
            if (occu=='tm'):
                armedforces=0           
                craftrepair=0           
                execmanagerial=0        
                farmingfishing=0        
                handlerscleaners=0      
                machineopinspct=0      
                otherservice=0          
                privhouseserv=0        
                profspecialty=0         
                protectiveserv=0        
                sales=0                  
                techsupport=0           
                transportmoving=1
            dph=request.form['dph']
            if(dph=='nif'):
                notinfamily=1           
                otherrelative=0     
                ownchild=0            
                unmarried=0            
                wife=0
            if(dph=='or'):
                notinfamily=0           
                otherrelative=1     
                ownchild=0            
                unmarried=0            
                wife=0    
            if(dph=='oc'):
                notinfamily=0           
                otherrelative=0     
                ownchild=1            
                unmarried=0            
                wife=0  
            if(dph=='um'):
                notinfamily=0           
                otherrelative=0     
                ownchild=0            
                unmarried=1            
                wife=0
            if(dph=='w'):
                notinfamily=0           
                otherrelative=0     
                ownchild=0            
                unmarried=0            
                wife=1
            it=request.form['it']
            if (it=='pc'):
                pc=1
                svc=0
                vt=0
            if (it=='svc'):
                pc=0
                svc=1
                vt=0
            if (it=='vt'):
                pc=0
                svc=0
                vt=1
            ct=request.form['ct']
            if (ct=='rc'):
                rc=1
                sc=0
            if (ct=='sc'):
                rc=0
                sc=1
            ac=request.form['ac']
            if (ac=='fire'):
                fire=1
                none=0
                other=0
                police=0
            if (ac=='none1'):
                fire=0
                none=1
                other=0
                police=0
            if (ac=='other'):
                fire=0
                none=0
                other=1
                police=0
            if (ac=='police'):
                fire=0
                none=0
                other=0
                police=1
            filename = 'rf_model.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            #predictions using the loaded model file
            prediction=loaded_model.predict([[nm,app,el,mg,ml,time,nvi,nbi,nwp,aci,
            acp,acv,p_csl,gn,eql,insvr,prd,polr,armedforces,craftrepair,
            execmanagerial,farmingfishing,handlerscleaners,machineopinspct,
            otherservice,privhouseserv,profspecialty,protectiveserv,sales,
            techsupport,transportmoving,notinfamily,otherrelative,
            ownchild,unmarried,wife,pc,svc,vt,rc,sc,fire,none,other,police]])
            print('prediction is', prediction)
            if prediction[0]==1:
                prediction="Fraud"
                elligible="Not Elligible"
            else:
                prediction="not Fraud"
                elligible="Elligible"
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction,elligible=elligible)
        except Exception as e:
            print('The Exception message is: ',e)
           
    # return render_template('results.html')
    else:
            return render_template('logged_in.html') 
        
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
