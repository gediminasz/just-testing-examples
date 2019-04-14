class Fooer
  def foo
    "foo"
  end
end

RSpec.describe Fooer do
  describe '#foo' do
    subject { fooer.foo }
    let(:fooer) { Fooer.new }

    it { is_expected.to eq("foo") }

    it { is_expected.to_not eq("bar") }
  end
end
