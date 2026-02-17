import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

const data = {

  AgeVsScreenTimeData: [],

}

const getters = {
	AgeVsScreenTimeData: (state) => state.AgeVsScreenTimeData,
};


const actions = {
};

const mutations = {
};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};