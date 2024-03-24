# Type Checking

## Activate the Types Environment

```bash
hatch -e types shell
```

## Generate Stubs

```bash
stubgen -p cowsay -o ./stubs
```

## Check Types

```bash
hatch run check
```