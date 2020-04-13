const foo = () => "foo";

test('returns foo', () => {
    expect(foo()).toBe("foo");
});

test('does not return bar', () => {
    expect(foo()).not.toBe("bar");
});
