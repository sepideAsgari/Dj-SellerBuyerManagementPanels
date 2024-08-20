<template>
    <div class="star-rating">
      <span v-for="n in maxStars" :key="n" @click="rate(n)" :class="{ 'filled': n <= rating }">&#9733;</span>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      maxStars: {
        type: Number,
        default: 5
      },
      rating: {
        type: Number,
        default: 0
      },
      readOnly: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      rate(stars) {
        if (!this.readOnly) {
          this.$emit('update:rating', stars);
        }
      }
    }
  };
  </script>
  
  <style>
  .star-rating {
    font-size: 24px;
  }
  
  .star-rating span {
    cursor: pointer;
  }
  
  .star-rating .filled {
    color: gold;
  }
  </style>
  