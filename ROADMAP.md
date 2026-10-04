# EmberVault Module SDK Roadmap

## Purpose

Provide the stable, dependency-free boundary every EmberVault module uses to
communicate with Control Center.

## Scope

Included: contracts integration, context/results, lifecycle, manifests,
capability and safety helpers, operation/recovery references, and fixtures.

Excluded: Control Center policy decisions, game access, UI, and live mutation.

## Dependencies

- EmberVault-Contracts: required shared schemas.
- Python packaging: required distribution path.

## Milestones

1. Contracts v1 integration and compatibility checks.
2. Lifecycle, result, manifest, safety, operation, recovery, and evidence APIs.
3. Starter module template and independent test suite.
4. Clean-install, package, and compatibility verification.
5. Release candidate and versioned documentation.

## Definition of done

- [ ] Every public API has tests and documentation.
- [ ] Invalid and blocked module states fail closed.
- [ ] Package builds in a clean environment.
- [ ] Starter module runs independently of Control Center.
- [ ] Contracts and SDK compatibility are explicit.
- [ ] Changes are committed and pushed.
