# FIGTR — MVP vs Future Entities

## Purpose

This document separates the database entities required for the initial MVP launch from those planned for future expansion. This guides development prioritization and scope.

## MVP Entities (Required for Initial Launch)

### Phase 1 — Identity & Tenancy

| Entity | Description |
|--------|-------------|
| User | Platform account. Can belong to multiple schools. |
| Role | Named role (admin, teacher, student, parent). |
| Permission | Granular permission assignable to roles. |
| Membership | Links a user to a school with a specific role. |
| School | The tenant. A school using the platform. |
| SchoolProfile | Extended profile/branding for a school. |
| SchoolSettings | Configuration settings for a school. |

### Phase 2 — School Structure

| Entity | Description |
|--------|-------------|
| AcademicSession | A school year or session. |
| Term | A term within an academic session. |
| Class | A class/grade level. |
| ClassArm | A specific arm/stream of a class. |
| Department | A department within the school. |
| Subject | A subject taught. |
| House | A school house. |
| GradingSystem | Defines grade scales and score ranges. |

### Phase 3 — People

| Entity | Description |
|--------|-------------|
| Student | A student enrolled in a school. |
| ParentGuardian | A parent or guardian of a student. |
| Teacher | A teacher employed by a school. |
| StaffProfile | Additional profile data for non-teaching staff. |
| StudentGuardianRelationship | Links a student to one or more guardians. |

### Phase 4 — Academics

| Entity | Description |
|--------|-------------|
| Attendance | Records student attendance. |
| Assessment | A continuous assessment (quiz, assignment). |
| Examination | A formal examination. |
| Result | A student's result for an assessment/examination. |
| ReportCard | A compiled report card for a student/term. |
| Promotion | Records a student's promotion to the next class. |
| AcademicRecord | A student's academic history. |

### Phase 5 — Finance

| Entity | Description |
|--------|-------------|
| FeeCategory | A category of fees. |
| FeeStructure | Defines fees for a class/session. |
| Invoice | An invoice issued to a student/guardian. |
| Payment | A payment made against an invoice. |
| Receipt | A receipt issued for a payment. |
| FinancialTransaction | A record of a financial transaction. |

### Phase 6 — Communication

| Entity | Description |
|--------|-------------|
| Announcement | A school-wide announcement. |
| Notification | A notification sent to a user. |
| Event | A school event. |
| Message | A message between users. |

### Phase 7 — Website Builder

| Entity | Description |
|--------|-------------|
| WebsiteSettings | Configuration for a school's public website. |
| Page | A page on the school's public website. |
| NewsPost | A news article on the school's website. |
| GalleryItem | An image/video in the school's gallery. |
| ContactSubmission | A contact form submission from the website. |

### Phase 8 — Platform Operations

| Entity | Description |
|--------|-------------|
| PlatformAdmin | Platform-level administrator accounts. |
| Subscription | Tenant subscription/billing records. |
| AuditLog | Audit trail for sensitive operations. |

---

## Future Expansion Entities

These entities are planned for future phases, after the MVP launch.

### Timetable / Scheduling

| Entity | Description |
|--------|-------------|
| Timetable | Class timetables and scheduling. |
| Period | A time period within the school day. |
| Lesson | A scheduled lesson. |

### Library

| Entity | Description |
|--------|-------------|
| Book | A library book. |
| BookCopy | A physical copy of a book. |
| LibraryLoan | A record of a book loan. |

### Transport

| Entity | Description |
|--------|-------------|
| Route | A transport route. |
| Vehicle | A school vehicle. |
| Trip | A scheduled trip. |

### Health

| Entity | Description |
|--------|-------------|
| HealthRecord | A student's health record. |
| MedicalVisit | A record of a medical visit. |
| Immunization | A record of immunization. |

### Inventory / Assets

| Entity | Description |
|--------|-------------|
| Asset | A school asset. |
| InventoryItem | An inventory item. |
| AssetAssignment | An asset assigned to a user/location. |

### Advanced Analytics

| Entity | Description |
|--------|-------------|
| AnalyticsReport | A generated analytics report. |
| DataWarehouse | A separate reporting database (future). |

### AI-Driven Features

| Entity | Description |
|--------|-------------|
| AIInsight | AI-generated insights (future). |
| PredictionModel | Predictive analytics models (future). |

---

*This document is a living artifact and will be updated as the product roadmap evolves.*