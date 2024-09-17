import paramiko

# SSH client yaratamiz
ssh = paramiko.SSHClient()

# SSH serverni tekshirish uchun known_hosts faylini tekshirishga ruxsat beramiz
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# SSH serverga ulanamiz
try:
    ssh.connect('192.168.1.109', username='kali', password='kali')
    print("Ulanish muvaffaqiyatli amalga oshirildi!")

    # Masofaviy buyruqni bajarish
    stdin, stdout, stderr = ssh.exec_command('ls -la')

    # Natijalarni chiqaramiz
    print(stdout.read().decode())

except paramiko.SSHException as e:
    print(f"SSH ulanishda xatolik: {e}")

finally:
    # SSH ulanishni yopamiz
    ssh.close()
