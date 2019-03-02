import Vue from 'vue'
import '@/plugins/vuetify'
import { AXIOS } from '@/util/http-commons'
import App from '@/App.vue'
import router from '@/router'


Vue.config.productionTip = false
Vue.prototype.$http = AXIOS
Vue.prototype.$crudEventbus = new Vue()
Vue.prototype.$snackbarEventbus = new Vue()

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

