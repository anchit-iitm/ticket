import { createStore } from 'vuex'

export default createStore({
  state: {
    userRole: '',
    // isAuthenticated: false,
  },
  getters: {
  },
  mutations: {
    setUserData(state, role) {
      state.userRole = role;
    },
    clearUserData(state) {
      // state.isAuthenticated = false;
      state.userRole = '';
    },
  },
  actions: {
  },
  modules: {
  }
})
