<template>
  <div>
    <div class="row my-2">
      <input type="text" v-model.trim="title" placeholder="리뷰 제목을 입력하세요">
    </div>
    <div class="row my-2">
      <input type="text" v-model.trim="rank" @keyup.enter="createReview" placeholder="1부터 5까지 평점을 입력하세요">
    </div>
    <div class="row my-2">
        <textarea rows="4" v-model.trim="content" placeholder="리뷰 내용을 입력하세요">
        </textarea>
    </div>
    <button type="button" class="btn" @click="createReview" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">Review Create</button>
  
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: "CreateReview",
  data: function () {
    return {
      title: null,
      content: null,
      rank: null,
    }
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview: function () {
      const reviewItem = {
        title: this.title,
        content: this.content,
        rank: this.rank
      }
      if (reviewItem.content) {
        axios({
          method: 'post',
          url: `https://ssafypedia.link/movies/${this.movie.id}/review/`,
          data: reviewItem,
          headers: this.setToken()
        })
        .then((res) => {
          console.log(res)
          this.title = null,
          this.content = null,
          this.rank = null,
          this.$emit('create-review')
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },

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