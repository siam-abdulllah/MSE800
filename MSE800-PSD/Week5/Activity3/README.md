# Clinic System Activity Diagram

This activity diagram represents a clinic system where a patient can book an appointment, pay the booking fee, and order medication after consultation.

## Activity Diagram (Mermaid)

```mermaid
flowchart TD
    start((Start))

    subgraph Patient
        P1[Request Appointment]
        P2[Select Slot and Details]
        P3[Pay Booking Fee]
        P4[Attend Consultation]
        P5[Order Medication]
    end

    subgraph Clinic
        C1[Display Available Slots]
        C2{Slot Available?}
        C3[Prompt Booking Fee]
        C4[Confirm Appointment]
        C5[Conduct Exam and Diagnose]
        C6[Issue Prescription]
        C7[Process Order and Notify]
    end

    endNode((End))

    start --> P1
    P1 --> C1
    C1 --> P2
    P2 --> C2
    C2 -- No --> C1
    C2 -- Yes --> C3
    C3 --> P3
    P3 --> C4
    C4 --> P4
    P4 --> C5
    C5 --> C6
    C6 --> P5
    P5 --> C7
    C7 --> endNode
```

## Brief Description

- The diagram is organized into two lanes: `Patient` and `Clinic`.
- The patient requests an appointment and selects a slot, while the clinic checks availability.
- If no slot is available, the flow loops back to displaying available slots.
- When available, the clinic prompts for payment and confirms the appointment after fee payment.
- After consultation and prescription, the patient orders medication and the clinic processes the order before ending the workflow.
