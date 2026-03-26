чел генерит ssh ключ:
```Bash
ssh-keygen -t ed25519
cat ~/.ssh/id_ed25519.pub
```

под `user1` на сервере:
```Bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```
Вставляешь ключ **новой строкой**.

Потом:
```Bash
chmod 700 ~/.ssh  
chmod 600 ~/.ssh/authorized_keys
```
