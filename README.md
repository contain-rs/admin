Administrative tools for the contain-rs organisation.

- `homu`: configuration and tools for Homu
  - `generate-cfg.py`: consumes `secrets.toml` and `configs.toml` to
    print a Homu `cfg.toml` to stdout. `configs.toml` contains the
    basic per-repo configuration (reviewers etc.) and is checked in,
    while `secrets.toml` contains application keys and user tokens and
    shouldn't be checked in. See `*.example.toml`.


Requires Python 3, and will work best in a Homu venv.
