export type parsed_date_result = {
  is_valid: boolean;
  value: Date | null;
  reason: string | null;
};

const iso_date_pattern = /^(\d{4})-(\d{2})-(\d{2})$/;

const valid_result = (value: Date): parsed_date_result => ({
  is_valid: true,
  value,
  reason: null,
});

const invalid_result = (reason: string): parsed_date_result => ({
  is_valid: false,
  value: null,
  reason,
});

function parse_iso_date(input: string): Date | null {
  const iso_match = iso_date_pattern.exec(input);
  if (!iso_match) {
    return null;
  }

  const year = Number(iso_match[1]);
  const month = Number(iso_match[2]);
  const day = Number(iso_match[3]);
  const parsed = new Date(Date.UTC(year, month - 1, day));

  // Guard against overflow (e.g., 2026-02-31 becoming March 3)
  if (
    parsed.getUTCFullYear() !== year ||
    parsed.getUTCMonth() !== month - 1 ||
    parsed.getUTCDate() !== day
  ) {
    return new Date(Number.NaN);
  }

  return parsed;
}

export function parse_date(input: string): parsed_date_result {
  const trimmed_input = input.trim();

  if (!trimmed_input) {
    return invalid_result('Input is empty.');
  }

  const parsed_iso_date = parse_iso_date(trimmed_input);
  if (parsed_iso_date !== null) {
    if (Number.isNaN(parsed_iso_date.getTime())) {
      return invalid_result('Invalid calendar date.');
    }
    return valid_result(parsed_iso_date);
  }

  const timestamp = Date.parse(trimmed_input);
  if (Number.isNaN(timestamp)) {
    return invalid_result('Unsupported date format.');
  }

  return valid_result(new Date(timestamp));
}
