import '@babel/polyfill'
import Vue from 'vue'
import Vuetify from 'vuetify'
import './plugins/vuetify'
import '@fortawesome/fontawesome-free/css/all.css'
import App from './App.vue'

Vue.config.productionTip = false
Vue.use(Vuetify, {
  iconfont: 'fa5'
})

new Vue({
  render: h => h(App),
}).$mount('#app')
