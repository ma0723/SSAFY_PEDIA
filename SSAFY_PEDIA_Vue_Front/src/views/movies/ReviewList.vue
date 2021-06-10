<template>
  <div> 
    <vue-glide
      v-if="reviews.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :breakpoints="{1500: {perView: 4}, 1399: {perView: 3}, 991: {perView: 2}, 800: {perView: 1}}"
    >
      <vue-glide-slide v-for="(review, idx) in reviews" :key="idx">
        <Review
          :review="review"
        />
      </vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import Review from '@/views/movies/Review'
export default {
  name: "ReviewList",
  components: {
    Review,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
  },
  props: {
    reviews: {
      type: Array,
    }
  },
}
</script>

<style>

</style>