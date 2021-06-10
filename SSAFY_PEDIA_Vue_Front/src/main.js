import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VueRouter from 'vue-router';
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'
// import VueSplide from '@splidejs/vue-splide';

// Vue.use( VueSplide );
Vue.use(VueGlide)

Vue.config.productionTip = false

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err;
	});
};

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
