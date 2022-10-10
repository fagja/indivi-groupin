@app.route("/trimming", methods=['GET', 'POST'])
def todb():
    if(request.is_json):
        data = request.get_json()
        nickname = data['nickname']
        birthdate = data['birthdate']
        sex = data['sex']
        residence = data['residence']
        love_target = data['love_target']
        email_address = data['email_address']

        img_base64 = post_img.split(',')[1]
    else:
        data= request.get_data().decode()
        temp = data.split('"')
        img_base64 = temp[3]
