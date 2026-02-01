export default function cleanSet(set, startString) {
  if (!startString) return '';

  const result = [...set] // convert Set to array
    .filter((value) => value.startsWith(startString)) // keep only matching
    .map((value) => value.slice(startString.length)) // remove the startString
    .join('-'); // join with dash

  return result;
}
