## Purpose

Lets a user select several todos at once and shift all of their due dates forward by a week in a single action, instead of editing each todo individually.

## ADDED Requirements

### Requirement: Select multiple todos for bulk rescheduling
The system SHALL let a user select any number of todos on the board, including zero, one, or all of them, before submitting a bulk reschedule action.

#### Scenario: Selecting several todos
- **WHEN** the user checks the selection control on three different todos and submits the bulk reschedule action
- **THEN** all three selected todos are included in the reschedule; unselected todos are not

### Requirement: Push selected todos' due dates forward by one week
The system SHALL, for each selected todo, set its `due_date` to 7 days after its current `due_date` when the bulk reschedule action is submitted.

#### Scenario: Single selected todo pushed a week forward
- **WHEN** a todo with `due_date` "2026-09-10" is selected and the bulk reschedule action is submitted
- **THEN** that todo's `due_date` becomes "2026-09-17"

#### Scenario: Multiple selected todos each pushed from their own due date
- **WHEN** todo A (`due_date` "2026-09-05") and todo B (`due_date` "2026-09-20") are both selected and the bulk reschedule action is submitted
- **THEN** todo A's `due_date` becomes "2026-09-12" and todo B's `due_date` becomes "2026-09-27"

### Requirement: Unselected todos are unaffected
The system SHALL leave the `due_date` and all other fields of any unselected todo unchanged when the bulk reschedule action is submitted.

#### Scenario: One todo selected among several
- **WHEN** only one of three existing todos is selected and the bulk reschedule action is submitted
- **THEN** the two unselected todos retain their original `due_date`

### Requirement: Submitting with no selection is a no-op
The system SHALL leave all todos unchanged, without error, when the bulk reschedule action is submitted with no todos selected.

#### Scenario: No todos selected
- **WHEN** the bulk reschedule action is submitted without checking any todo
- **THEN** no todo's `due_date` changes and the board reloads normally

### Requirement: Selecting a nonexistent id is a no-op for that id
The system SHALL ignore any selected id that does not match an existing todo, without error, and still apply the reschedule to selected ids that do match.

#### Scenario: Stale id mixed with a valid selection
- **WHEN** the bulk reschedule action is submitted with one valid todo id and one id that no longer exists
- **THEN** the valid todo's `due_date` is pushed forward by a week and no error occurs
