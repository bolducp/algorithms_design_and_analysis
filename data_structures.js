function Stack() {
  return {
    items: [],
    push: function(item) {
      this.items.push(item);
    },
    pop: function() {
      return this.items.pop();
    }
  }
}

function Queue() {
  return {
    items: [],
    push: function(item) {
      this.items.push(item);
    },
    next: function() {
      return this.items.shift();
    }
  }
}
