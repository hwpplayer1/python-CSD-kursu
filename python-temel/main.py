def user_input():
    # Kayıtlı kullanıcı adı ve şifre
    registered_user = "kullanici"
    stored_password = "sifre123"

    # Kullanıcıdan bilgileri alma
    user_name = input("Kullanıcı Adı: ")
    password = input("Şifre: ")

    # Kullanıcı adı ve şifre kontrolü
    if user_name == registered_user and password == stored_password:
        print("Giriş başarılı! Hoş geldiniz, {}.".format(user_name))
    else:
        print("Hatalı kullanıcı adı veya şifre. Tekrar deneyin.")

# Kullanıcı girişi fonksiyonunu çağırma
user_input()
