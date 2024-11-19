## Second part

- [ ] Validate each field
      **where does it go that validation logic?**
      **class based approach**: Passport is a class.

  - Required fields use a constructor for each field which contains the validation logic for each field
  - it has a method validation to validate itself

    **Procedural approach**

  - validate_doc function
  - validate_doc has helpers functions to validate each field
  - return true when all of the functions validate to true
