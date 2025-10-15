# CRM Custom Lead (C2Q)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![Odoo](https://img.shields.io/badge/Odoo-17%20%7C%2018-blue.svg)
![License](https://img.shields.io/badge/license-LGPL--3.0-lightgrey.svg)
[![C2Q](https://img.shields.io/badge/Made%20by-C2Q%20Developers-0B0F16?logo=python&logoColor=white)](https://c2q.com.ec)

---

### Módulo: **CRM Custom Lead (C2Q)**  
*Potenciador ligero para CRM con flujo guiado, campañas simples y una importación de ubicaciones de Ecuador segura y sin fricciones.*

---

## 🧭 Resumen

Este módulo mejora el CRM estándar de Odoo para equipos comerciales que requieren **usabilidad inmediata** y **flujo controlado** sin configuraciones complejas.  
Incluye validaciones, automatizaciones y gestión jerárquica de ubicaciones del Ecuador (País → Provincia → Ciudad → Parroquia).

---

## ⚙️ Funcionalidades principales

### 🔹 Leads claros y completos
- Campos útiles: titular, documentos, contacto, referencias, dirección y pago.  
- Generación automática del nombre (“Oportunidad N”).  
- Asignación automática del asesor según usuario/empleado.  

### 🔹 Flujo guiado por etapas
- Etapas estándar: **Registro → Validación → Seguimiento → Cierre.**  
- Validaciones automáticas de cédula/RUC, teléfono y correo.  
- Control de avance basado en cumplimiento de requisitos mínimos.  

### 🔹 Campañas CRM simplificadas
- Modelo propio de campañas.  
- Solo perfiles autorizados pueden crear o editar.  

### 🔹 Importación de ubicaciones (Ecuador)
- Compatible con el importador estándar de Odoo.  
- Evita duplicados:  
  - Parroquias únicas por ciudad.  
  - Ciudades únicas por provincia.  
- Crea automáticamente provincias y ciudades inexistentes con país “Ecuador (EC)”.  

### 🔹 Experiencia de uso
- “Quick create” optimizado y asesor en solo lectura.  
- Barra global oculta para asesores.  
- Menús sensibles (Apps, Empleados) visibles solo para usuarios con permiso.  

---

## 🧩 Instalación y uso

### **Cómo empezar**
1. **Leads personalizados:**  
   `CRM → Leads Personalizados → Crear`  
   Completa las pestañas y deja que el sistema valide y avance etapas.

2. **Campañas personalizadas:**  
   `CRM → Campañas Personalizadas → Crear`

3. **Importar ubicaciones:**  
   `CRM → Locación → Ubicaciones → Importar`

   | CSV Column | Campo Odoo |
   |-------------|-------------|
   | `City` | Ciudad (Import) |
   | `State` | Provincia (Import) |
   | `Country` | Country (EC o Ecuador) |
   | `Name` | Parroquia |
   | `Zip` | (opcional) |

---

## 🔐 Roles y seguridad
Perfiles incluidos:
> Asesor · Validador · Post-venta · Back-office · Gerente · Jefe de Operaciones · Supervisor

Al asignar uno de estos perfiles, el usuario se configura automáticamente como **Interno**, eliminando roles *Portal* y *Público* para evitar conflictos.

---

## 🧮 Compatibilidad
- **Versiones:** Odoo 17 y 18  
- **Dependencias:** `base`, `crm`, `contacts`  

---

## 📄 Licencia

Este repositorio se distribuye bajo la licencia [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html).

---

## 🧑‍💻 Créditos

**Desarrollado por [C2Q](https://c2q.com.ec)**  
*IT · Development · Software · Cybersecurity*  
📩 [info@c2q.com.ec](mailto:info@c2q.com.ec)

> “Innovando soluciones, construyendo el futuro.”  
> © 2025 C2Q. Todos los derechos reservados.

---
