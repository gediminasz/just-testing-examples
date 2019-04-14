class Barer
  def bar
    "bar"
  end
end

RSpec.describe Barer do
  describe '#bar' do
    subject { barer.bar }
    let(:barer) { Barer.new }

    it "returns bar" do
      expect(subject).to eq("bar")
    end

    it "does not return foo" do
      expect(subject).to_not eq("foo")
    end
  end
end
