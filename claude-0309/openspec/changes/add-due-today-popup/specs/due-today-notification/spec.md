## Purpose

Surfaces todos due today as a popup notification when the todo board is opened, so a user cannot open the board and miss something due right now without scanning every row.

## ADDED Requirements

### Requirement: Popup shown for todos due today
The system SHALL display a popup notification when the todo board loads if one or more incomplete todos have a `due_date` equal to the current date. The popup SHALL list the text of each such todo.

#### Scenario: One todo due today
- **WHEN** the todo board is opened and exactly one incomplete todo has `due_date` equal to today
- **THEN** a popup notification appears listing that todo's text

#### Scenario: Multiple todos due today
- **WHEN** the todo board is opened and more than one incomplete todo has `due_date` equal to today
- **THEN** a popup notification appears listing all of their texts

### Requirement: Popup suppressed when nothing is due today
The system SHALL NOT display the popup notification when no incomplete todo has `due_date` equal to today.

#### Scenario: No todos due today
- **WHEN** the todo board is opened and no todo has `due_date` equal to today
- **THEN** no popup notification appears

#### Scenario: Todo due today but already done
- **WHEN** the todo board is opened and the only todo with `due_date` equal to today has `done` set to true
- **THEN** no popup notification appears

### Requirement: Popup is dismissible without a page reload
The system SHALL let the user close the popup notification without submitting a form to the server or navigating away from the current page.

#### Scenario: User dismisses the popup
- **WHEN** the popup notification is visible and the user activates its close control
- **THEN** the popup notification closes and the todo list underneath remains visible, with no new page load

### Requirement: No JavaScript or persisted dismissal state
The system SHALL implement the popup using plain HTML rendered by the server, without JavaScript and without storing dismissal state in `todos.json` or elsewhere, consistent with the project's full-page-reload design.

#### Scenario: Popup reappears on next visit
- **WHEN** the user dismisses the popup, then reloads or reopens the todo board while the same todo is still incomplete and still due today
- **THEN** the popup notification appears again
