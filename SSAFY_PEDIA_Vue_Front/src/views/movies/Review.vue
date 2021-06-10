<template>
  <div class="card" style="width: 18rem;" :class="{ dark: isDark, light: isLight }">
    <div class="card-body">
      <h5 class="card-title text-nowrap overflow-hidden">{{ review.title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted text-nowrap overflow-hidden">
        {{review.movie_title}}
        <span v-for="(i, idx) in rating" :key="idx">
          <i style="color:yellow;" class="fas fa-star"></i>
        </span> 
      </h6>
      <p class="card-text text-nowrap overflow-hidden">{{ review.content }}</p>
      <button type="button" class="btn" @click="reviewDetail" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">Review Detail</button>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: "Review",
  data: function () {
    return {
      rating: 0,
      movie: null,
    }
  },
  props: {
    review: {
      type: Object,
      required: true,
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    reviewMovie: function () {
      axios({
        method: 'get',
        url: `https://ssafypedia.link/movies/${Number(this.review.movie)}/`,
        // 영화 pk는 정수형 입력 Number()
        headers: this.setToken()
      })
      .then((res) => {
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    ratingToInt: function () {
      this.rating = Math.floor(Number(this.review.rank))
      // str을 숫자로 변환 후 Number() 
      // 내림 함수 Math.floor()
    },
    reviewDetail: function () {
      this.$router.push({ name: "ReviewDetail", query: { review: this.review, movie: this.movie }} )
    },
  },
  created: function () {
    this.ratingToInt()
    this.reviewMovie()
  },
  computed: {
    isDark: function () {
      return this.$store.getters.isDark
    },
    isLight: function () {
      return this.$store.getters.isLight
    },
  },
}
</script>

<style>

</style>