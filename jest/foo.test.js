const foo = () => "foo";

describe(foo, () => {
    it('returns foo', () => {
        expect(foo()).toBe("foo");
    });

    it('does not return bar', () => {
        expect(foo()).not.toBe("bar");
    });
});
