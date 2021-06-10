<template>
  <div class="col">
    <vue-glide
      v-if="movies.length"
      class="glide__track"
      data-glide-el="track"
      ref="slider"
      type="slider"
      :autoplay="true"
      :animationDuration="1500"
      :breakpoints="{5000: {perView: 4}, 2000: {perView: 3}, 1399: {perView: 2}, 991: {perView: 1}}"
    >
      <vue-glide-slide
        v-for="(movie, idx) in movies"
        :key="idx">
        <MbtiList
          :movie="movie"
        />
      </vue-glide-slide>
    </vue-glide>
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import MbtiList from '@/views/mbtis/MbtiList.vue'

export default {
  name: "Mbtis",
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  components: {
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    MbtiList,
  },
  methods: {
  }
}
</script>

<style>

</style>