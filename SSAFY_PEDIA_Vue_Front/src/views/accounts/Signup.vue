<template>
  <div>
    <p class="title-font">Signup Page</p>
    <div class="container">
      <div class="mt-2">
        <label class="title-font mx-2" for="username">ID: </label>
        <input type="text" id="username" v-model="credentials_pass.username">
      </div>
      <div class="mt-2">
        <label class="title-font mx-2" for="firstName">First Name: </label>
        <input type="text" id="firstName" v-model="credentials_pass.first_name">
      </div>
      <div class="mt-2">
        <label class="title-font mx-2" for="lastName">Last Name: </label>
        <input type="text" id="lastName" v-model="credentials_pass.last_name">
      </div>
      <div class="mt-2">
        <label class="title-font mx-2" for="password">Password: </label>
        <input type="password" id="password" v-model="credentials_pass.password">
      </div>
      <div class="mt-2">
        <label class="title-font mx-2" for="passwordConfirmation">Password Confirmation: </label>
        <input type="password" id="passwordConfirmation" v-model="credentials_pass.passwordConfirmation">
      </div>
      <button type="button" class="btn mt-5" @click="signup(credentials_pass)" :class="{ 'btn-outline-dark': isLight, 'btn-outline-light': isDark }">SIGN UP</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials_pass: {
        username: null,
        password: null,
        passwordConfirmation: null,
        first_name: null,
        last_name:null,
      }  
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'https://ssafypedia.link/accounts/signup/',
        data: this.credentials_pass,
      })
      .then(res => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch(err => {
        console.log(err)
      })
    }
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
