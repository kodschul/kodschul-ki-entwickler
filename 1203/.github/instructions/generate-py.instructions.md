---
description: when generating python code, follow these guidelines:
applyTo: '**/*.py'
---

<!-- Tip: Use /create-instructions in chat to generate content with agent assistance -->

always use camelCase for variable and function names, and PascalCase for class names. Do not use underscores in variable or function names. For example, use `myVariable` instead of `my_variable`, and `MyClass` instead of `my_class`.

if the user wants to override the default code style ask them to verify that they want to use snake_case instead of camelCase for variable and function names, and that they want to use snake_case instead of PascalCase for class names. If they confirm, then use snake_case for variable and function names, and snake_case for class names. For example, use `my_variable` instead of `myVariable`, and `my_class` instead of `MyClass`.
