const bar = () => "bar";

test("should return bar", () => {
    expect(bar()).toBe("bar");
});

test("should not return foo", () => {
    expect(bar()).not.toBe("foo");
});
