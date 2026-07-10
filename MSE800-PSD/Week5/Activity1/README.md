# Week 5 Activity 1 — Money Exchange use cases

This folder contains UML-style use case diagrams for a **Money Exchange** application, drawn in [diagrams.net](https://app.diagrams.net/) (`.drawio`).

## Combined diagram (recommended)

| File | Description |
|------|-------------|
| `UseCaseDiagram_Combined.drawio` | **Single diagram** merging customer self-service and bank administration: one shared header (purpose, actors, short scenarios) and two system boundaries side by side. |

Open the combined file in diagrams.net and use a wide canvas or horizontal scroll; page size is set for **2480 × 920** px.

## Original split diagrams

| File | Description |
|------|-------------|
| `UseCaseDiagram1_CustomerMoneyServices.drawio` | Customer-facing use cases: authentication, balances, quotes, exchange, history, profile; external rate provider. |
| `UseCaseDiagram2_BankAdministration.drawio` | Operations: currency catalog, exchange rates, accounts and `ACC_CUST` links, transaction log search/export, corrections with compliance approval; scheduled batch job. |

PNG exports (if present) match the same names with a `.png` suffix.

## Customer and administrator interaction

Customers normally use only the **customer boundary**, but **account linking** (`ACC_CUST`) is a shared concern: the **customer** requests or confirms linkage while the **bank administrator** performs the back-office **Link / unlink customer to account** use case. In the combined diagram this is shown as a dashed association from **Customer** to that operations use case.

## Actors and boundaries

- **Customer** — uses the customer boundary (left in the combined diagram).
- **External Rate Provider** («System») — supplies reference rates for customer quotes.
- **Bank Administrator** — maintains catalog, rates, accounts, and log corrections.
- **Compliance Officer** — reviews logs and may approve high-value corrections.
- **Scheduled Job** («System») — stages or imports rate data toward publishing rates.

## Relationships (UML)

- **`«include»`** — the base use case always brings in the included behavior (e.g. executing an exchange includes getting a quote and validating balance).
- **`«extend»`** — optional or conditional addition (e.g. sending confirmation extends a successful exchange; approving a correction extends the correction flow when thresholds apply).

## Short scenarios

**Customer (A):** Authenticate → request exchange quote → system validates source balance → execute exchange → record transaction and send confirmation → customer views transaction history later.

**Operations (B):** Maintain currency catalog and publish rates (batch may stage data) → search transaction log → correct an erroneous entry with reason and evidence → compliance approves high-value corrections before the update is finalized.

## Editing

1. Open any `.drawio` file in diagrams.net (or VS Code with a Draw.io extension).
2. Adjust layout, colors, or wording as needed for your submission.
3. Export to PNG/PDF from the app if your course requires a static image.
