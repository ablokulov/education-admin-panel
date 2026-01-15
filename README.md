# education-admin-panel

### Loyiha turi: Admin Panel

Foydalanuvchi turi: faqat 1 ta admin

Ma’lumot almashish: REST API (JSON)

🔐 Autentifikatsiya (Login)

Tizimga faqat bitta admin kira oladi

Admin:

username (yoki email)

password

Login majburiy (register yo‘q)

Admin parolini:

admin panel orqali o‘zgartirish mumkin

Password:

hashlangan holda saqlanishi kerak (bcrypt)

Token talablari:

Access token: 15 daqiqa

Refresh token: 30 kun

Refresh token HttpOnly cookie orqali saqlanishi kerak

Himoyalangan endpointlar uchun auth middleware

### 📌 Asosiy funksiyalar
### 1️⃣ Admin login
```

POST /api/auth/login

POST /api/auth/logout

POST /api/auth/refresh

POST /api/auth/change-password
```

### 2️⃣ Guruhlar bilan ishlash

Admin quyidagilarni qila olishi kerak:

Guruh qo‘shish

Guruhni tahrirlash

Guruhni o‘chirish

Guruhlar ro‘yxatini olish

## Guruh modeli:
```

id

name (guruh nomi)

teacherName (ixtiyoriy)

createdAt
```
```
Endpointlar:

POST /api/groups

GET /api/groups

PUT /api/groups/:id

DELETE /api/groups/:id
```

### 3️⃣ O‘quvchilar bilan ishlash

Admin quyidagilarni qila olishi kerak:

O‘quvchi qo‘shish

O‘quvchini tahrirlash

O‘quvchini o‘chirish

O‘quvchilar ro‘yxatini ko‘rish

O‘quvchini guruhga biriktirish

O‘quvchi modeli:
```

id

fullName

phone

groupId

createdAt
```

## Endpointlar:
```

POST /api/students

GET /api/students

PUT /api/students/:id

DELETE /api/students/:id
```