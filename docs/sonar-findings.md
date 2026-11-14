# SonarCloud Findings Triage - Alumni Management System

| # | Rule Name | File / Line | Severity | Risk Explanation |
|---|-----------|-------------|----------|------------------|
| 1 | Add an "id" attribute to this input field and associate it with a label | `alumni.html` / L32 | Major (Medium) | Screen readers cannot correctly identify the input field, making the form inaccessible for visually impaired users. |
| 2 | A form label must be associated with a control and have accessible text | `register.html` / L25 | Major (Medium) | Users relying on assistive technology will not know what data to enter, violating basic web accessibility standards. |
| 3 | Add an "id" attribute to this input field and associate it with a label | `register.html` / L30 | Major (Medium) | The lack of an ID means the label is not linked to the input, reducing usability and accessibility. |
| 4 | Add an "id" attribute to this input field and associate it with a label | `login.html` / L22 | Major (Medium) | Without an ID, automated testing tools and screen readers fail to associate the text with the input box. |
| 5 | A form label must be associated with a control and have accessible text | `login.html` / L18 | Major (Medium) | Forms without proper labels are difficult to navigate using keyboard-only controls. |
| 6 | Add an "id" attribute to this input field and associate it with a label | `index.html` / L45 | Major (Medium) | Missing IDs on inputs breaks the connection between the label and the input box. |
| 7 | A form label must be associated with a control and have accessible text | `index.html` / L50 | Major (Medium) | Input fields without accessible labels are a major accessibility violation. |
| 8 | Add an "id" attribute to this input field and associate it with a label | `contact.html` / L20 | Major (Medium) | The input field is not linked to its label, making it difficult for screen readers to parse. |