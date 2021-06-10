<template>
  <div class="container">
    <div class="row">
      <vue-glide
        v-if="movies.length"
        class="glide__track"
        data-glide-el="track"
        ref="slider"
        type="slider"
        :autoplay="true"
        :animationDuration="1500"
        :breakpoints="{10000: {perView: 9}, 4000: {perView: 7}, 3000: {perView: 6}, 1500: {perView: 5}, 1200: {perView: 4}, 991: {perView: 3}, 800: {perView: 2}}"
      >
        <vue-glide-slide
          v-for="(movie, idx) in movies"
          :key="idx">
          <MovieList
            :movie="movie"
          />
        </vue-glide-slide>
      </vue-glide>
    </div>
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieList from '@/views/movies/MovieList.vue'

export default {
  name: "Movies",
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  components: {
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    MovieList,
  },
  methods: {
    aaa: function () {
      console.log(this.movie)
      this.$router.push({ name: 'MovieDetail', query: { movie: this.movie } })
    }
  }
}
</script>

<style>

</style>