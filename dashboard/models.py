from django.db import models
from Crypto.Cipher import AES
from secrets import token_bytes

# Create your models here.
class CaesarEncrypt(models.Model):
    message = models.CharField(max_length=200)
    encrypted_message = models.CharField(max_length=200, blank=True)
    key = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'CAESAR'

    def save(self, *args, **kwargs):
        result = ""
        for i in range(len(self.message)):
            char = self.message[i]
            if (char.isupper()):
                result += chr((ord(char) + self.key-65) % 26 + 65)
            else:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
        self.encrypted_message = result
        return super().save(*args, **kwargs)




class AESEncrypt(models.Model):
    message = models.CharField(max_length=200)
    encrypted_message = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'AES'

    def save(self, *args, **kwargs):
        key = token_bytes(16)

        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(self.message.encode('ascii'))
        nonce, ciphertext, tag 
        self.encrypted_message = ciphertext
        return super().save(*args, **kwargs)



class cautionModel(models.Model):
    name = models.CharField(max_length=(200))
    number = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Caution'