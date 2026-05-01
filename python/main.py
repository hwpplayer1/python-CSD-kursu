"""
Experimental code from Google ai

MIT License

Copyright (c) 2026 Mass Collaboration Labs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os

while True:
    # Girdiyi komut ve dosya adı olarak ikiye bölüyoruz
    user_input = input('PSD>').strip().split(maxsplit=1)
    
    if not user_input:
        continue
        
    cmd = user_input[0]
    # Eğer yanına bir şey yazıldıysa target değişkenine atıyoruz
    target = user_input[1] if len(user_input) > 1 else None

    match cmd:
        case 'delete' | 'remove' | 'erase':
            if target:
                try:
                    if os.path.exists(target):
                        os.remove(target)
                        print(f'"{target}" dosyası başarıyla silindi.')
                    else:
                        print(f'Hata: "{target}" adında bir dosya bulunamadı.')
                except Exception as e:
                    print(f'İşlem sırasında bir hata oluştu: {e}')
            else:
                print("Lütfen silinecek dosya adını belirtin: delete dosya.txt")
                
        case 'exit' | 'quit':
            print("Çıkış yapılıyor...")
            break
            
        case _:
            print('Geçersiz komut. (delete, copy, rename, exit)')
