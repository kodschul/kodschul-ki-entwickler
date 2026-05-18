## ADDED Requirements

### Requirement: User can add a new todo
The system SHALL provide an input field and a submit action that creates a new todo entry in the list.

#### Scenario: Submit a valid todo title
- **WHEN** the user types a non-empty title into the input field and submits the form
- **THEN** a new todo with that title SHALL appear at the top of the todo list with `completed: false`

#### Scenario: Input is cleared after submission
- **WHEN** a todo is successfully added
- **THEN** the input field SHALL be cleared and focused, ready for the next entry

#### Scenario: Empty title is rejected
- **WHEN** the user submits the form with an empty or whitespace-only title
- **THEN** no todo SHALL be added and the input field SHALL remain unchanged

### Requirement: Todos are persisted across page refreshes
The system SHALL store the todo list in localStorage so that todos survive a browser refresh.

#### Scenario: Todos persist after reload
- **WHEN** the user adds one or more todos and then reloads the page
- **THEN** all previously added todos SHALL still appear in the list in their original order
