# FIGTR — Entity Relationship Diagram (ERD)

## Overview

This document provides a text-based entity relationship diagram for the FIGTR database. It describes the core entities, their purpose, main relationships, and tenant ownership, following the membership-based multi-tenancy model.

## Multi-Tenancy Core

```
User
  |
  |--< Membership >-- School
  |                      |
  |                      |--< School-owned records
```

- A **User** can have many **Memberships**.
- A **Membership** links a **User** to a **School** with a specific **Role**.
- A **School** owns all school-scoped data.

---

## Identity

### User

- **Purpose:** A platform account. Can belong to multiple schools.
- **Main relationships:** Has many Memberships; receives Notifications; sends/receives Messages.
- **School tenant:** No — platform-level entity.

### Role

- **Purpose:** A named role (e.g., admin, teacher, student, parent).
- **Main relationships:** Assigned to Memberships; has many Permissions (many-to-many).
- **School tenant:** No — platform-level entity (roles are predefined).

### Permission

- **Purpose:** A granular permission that can be assigned to roles.
- **Main relationships:** Belongs to many Roles (many-to-many).
- **School tenant:** No — platform-level entity.

### Membership

- **Purpose:** Links a user to a school with a specific role.
- **Main relationships:** Belongs to a User; belongs to a School; has a Role.
- **School tenant:** Yes — scoped to a School.

```
User
  |
  |--< Membership >-- School
  |       |
  |       |-- Role
  |              |
  |              |--< Permission
```

---

## School Management

### School

- **Purpose:** The tenant. A school that uses the platform.
- **Main relationships:** Has many Memberships, Students, Teachers, Classes, AcademicSessions, Subjects, Departments, Houses, GradingSystems, FeeCategories, Announcements, Events, WebsiteSettings, Pages, NewsPosts, GalleryItems, ContactSubmissions.
- **School tenant:** Yes — the root tenant entity.

### SchoolProfile

- **Purpose:** Extended profile/branding information for a school.
- **Main relationships:** Belongs to a School (one-to-one).
- **School tenant:** Yes.

### SchoolSettings

- **Purpose:** Configuration settings for a school.
- **Main relationships:** Belongs to a School (one-to-one).
- **School tenant:** Yes.

### AcademicSession

- **Purpose:** A school year or session (e.g., 2025/2026).
- **Main relationships:** Belongs to a School; has many Terms.
- **School tenant:** Yes.

### Term

- **Purpose:** A term within an academic session (e.g., First Term).
- **Main relationships:** Belongs to an AcademicSession.
- **School tenant:** Yes (via AcademicSession → School).

### Class

- **Purpose:** A class/grade level (e.g., Grade 5, JSS 1).
- **Main relationships:** Belongs to a School; has many ClassArms; has many Students.
- **School tenant:** Yes.

### ClassArm

- **Purpose:** A specific arm/stream of a class (e.g., Grade 5A).
- **Main relationships:** Belongs to a Class.
- **School tenant:** Yes (via Class → School).

### Department

- **Purpose:** A department within the school (e.g., Sciences).
- **Main relationships:** Belongs to a School; has many Subjects.
- **School tenant:** Yes.

### Subject

- **Purpose:** A subject taught (e.g., Mathematics).
- **Main relationships:** Belongs to a School; belongs to a Department; taught by many Teachers (many-to-many).
- **School tenant:** Yes.

### House

- **Purpose:** A school house (e.g., Red House, Blue House).
- **Main relationships:** Belongs to a School; has many Students.
- **School tenant:** Yes.

### GradingSystem

- **Purpose:** Defines grade scales and score ranges.
- **Main relationships:** Belongs to a School; used by Results/ReportCards.
- **School tenant:** Yes.

```
School
├── SchoolProfile
├── SchoolSettings
├── AcademicSession
│   └── Term
├── Class
│   └── ClassArm
├── Department
│   └── Subject
├── House
└── GradingSystem
```

---

## People

### Student

- **Purpose:** A student enrolled in a school.
- **Main relationships:** Belongs to a School; belongs to a Class; has many Guardians (via StudentGuardianRelationship); has many Results, Attendance, Invoices, ReportCards, Promotions, AcademicRecords.
- **School tenant:** Yes.

### ParentGuardian

- **Purpose:** A parent or guardian of a student.
- **Main relationships:** Linked to many Students (via StudentGuardianRelationship).
- **School tenant:** Yes (linked to students within a school).

### Teacher

- **Purpose:** A teacher employed by a school.
- **Main relationships:** Belongs to a School; teaches many Subjects (many-to-many); takes Attendance.
- **School tenant:** Yes.

### StaffProfile

- **Purpose:** Additional profile data for non-teaching staff.
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

### StudentGuardianRelationship

- **Purpose:** Links a student to one or more guardians.
- **Main relationships:** Belongs to a Student; belongs to a ParentGuardian.
- **School tenant:** Yes (via Student → School).

```
School
├── Student
│   ├── StudentGuardianRelationship ── ParentGuardian
│   └── AcademicRecord
├── Teacher
│   └── Subject (teaches, many-to-many)
└── StaffProfile
```

---

## Academic

### Attendance

- **Purpose:** Records student attendance for a class/date.
- **Main relationships:** Belongs to a Student; belongs to a Class; recorded by a Teacher.
- **School tenant:** Yes.

### Assessment

- **Purpose:** A continuous assessment (e.g., quiz, assignment).
- **Main relationships:** Belongs to a School; belongs to a Class/Subject; has many Results.
- **School tenant:** Yes.

### Examination

- **Purpose:** A formal examination.
- **Main relationships:** Belongs to a School; belongs to a Class/Subject; has many Results.
- **School tenant:** Yes.

### Result

- **Purpose:** A student's result for an assessment/examination.
- **Main relationships:** Belongs to a Student; belongs to an Assessment or Examination; uses a GradingSystem.
- **School tenant:** Yes.

### ReportCard

- **Purpose:** A compiled report card for a student/term.
- **Main relationships:** Belongs to a Student; belongs to a Term; contains many Results.
- **School tenant:** Yes.

### Promotion

- **Purpose:** Records a student's promotion to the next class.
- **Main relationships:** Belongs to a Student; belongs to a School; references from/to Classes.
- **School tenant:** Yes.

### AcademicRecord

- **Purpose:** A student's academic history/record.
- **Main relationships:** Belongs to a Student; belongs to a School.
- **School tenant:** Yes.

```
Student
├── Attendance
├── Result
│   ├── Assessment
│   └── Examination
├── ReportCard
├── Promotion
└── AcademicRecord
```

---

## Finance

### FeeCategory

- **Purpose:** A category of fees (e.g., tuition, boarding).
- **Main relationships:** Belongs to a School; has many FeeStructures.
- **School tenant:** Yes.

### FeeStructure

- **Purpose:** Defines fees for a class/session.
- **Main relationships:** Belongs to a School; belongs to a FeeCategory; belongs to a Class/AcademicSession.
- **School tenant:** Yes.

### Invoice

- **Purpose:** An invoice issued to a student/guardian.
- **Main relationships:** Belongs to a School; belongs to a Student; has many Payments.
- **School tenant:** Yes.

### Payment

- **Purpose:** A payment made against an invoice.
- **Main relationships:** Belongs to an Invoice; has one Receipt; has many FinancialTransactions.
- **School tenant:** Yes.

### Receipt

- **Purpose:** A receipt issued for a payment.
- **Main relationships:** Belongs to a Payment (one-to-one).
- **School tenant:** Yes.

### FinancialTransaction

- **Purpose:** A record of a financial transaction.
- **Main relationships:** Belongs to a Payment; belongs to a School.
- **School tenant:** Yes.

```
Student
└── Invoice
    └── Payment
        ├── Receipt
        └── FinancialTransaction
```

---

## Communication

### Announcement

- **Purpose:** A school-wide announcement.
- **Main relationships:** Belongs to a School; created by a User.
- **School tenant:** Yes.

### Notification

- **Purpose:** A notification sent to a user.
- **Main relationships:** Belongs to a User; may relate to a School.
- **School tenant:** Yes (when school-scoped).

### Event

- **Purpose:** A school event (e.g., sports day, PTA meeting).
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

### Message

- **Purpose:** A message between users.
- **Main relationships:** Sent by a User; received by a User; may relate to a School.
- **School tenant:** Yes (when school-scoped).

```
School
├── Announcement
├── Event
├── Notification ── User
└── Message ── User
```

---

## Website Builder

### WebsiteSettings

- **Purpose:** Configuration for a school's public website.
- **Main relationships:** Belongs to a School (one-to-one).
- **School tenant:** Yes.

### Page

- **Purpose:** A page on the school's public website.
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

### NewsPost

- **Purpose:** A news article on the school's website.
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

### GalleryItem

- **Purpose:** An image/video in the school's gallery.
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

### ContactSubmission

- **Purpose:** A contact form submission from the website.
- **Main relationships:** Belongs to a School.
- **School tenant:** Yes.

```
School
├── WebsiteSettings
├── Page
├── NewsPost
├── GalleryItem
└── ContactSubmission
```

---

## Relationship Summary

| Relationship | Type | Description |
|--------------|------|-------------|
| School → Student | One-to-Many | A school has many students |
| School → Teacher | One-to-Many | A school has many teachers |
| Student → School | Many-to-One | A student belongs to a school |
| Student → Guardian | Many-to-Many | A student can have many guardians (via StudentGuardianRelationship) |
| Student → Result | One-to-Many | A student has many results |
| Teacher → Subject | Many-to-Many | A teacher teaches many subjects |
| School → AcademicSession | One-to-Many | A school has many academic sessions |
| Invoice → Student | Many-to-One | An invoice belongs to a student |
| Payment → Invoice | Many-to-One | A payment belongs to an invoice |

---

*This document is a living artifact and will be refined as the data model evolves.*