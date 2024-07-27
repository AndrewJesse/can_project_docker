<template>
  <div class="home">
    <h1>Controlller Area Network bus data</h1>
    <table>
      <thead>
        <tr>
          <th @click="sortTable('timestamp')">
            Timestamp
            <span :class="getSortClass('timestamp')"></span>
          </th>
          <th @click="sortTable('data')">
            Data
            <span :class="getSortClass('data')"></span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="message in sortedMessages" :key="message.arbitration_id">
          <td>{{ message.timestamp }}</td>
          <td>{{ message.data }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      messages: [],
      currentSort: 'timestamp',
      currentSortDir: 'asc'
    };
  },
  computed: {
    sortedMessages() {
      return this.messages.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === 'desc') modifier = -1;
        if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        return 0;
      });
    }
  },
  created() {
    this.fetchMessages();
  },
  methods: {
    async fetchMessages() {
      try {
        const response = await axios.get('http://localhost:8000/messages');
        this.messages = response.data;
      } catch (error) {
        console.error('Error fetching messages:', error);
      }
    },
    sortTable(column) {
      if (this.currentSort === column) {
        this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
      }
      this.currentSort = column;
    },
    getSortClass(column) {
      if (this.currentSort === column) {
        return this.currentSortDir === 'asc' ? 'arrow-up' : 'arrow-down';
      }
      return '';
    }
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th {
  cursor: pointer;
  background: #f4f4f4;
  position: relative;
}
th span {
  margin-left: 5px;
}
.arrow-up::after {
  content: '▲';
}
.arrow-down::after {
  content: '▼';
}
th, td {
  padding: 8px;
  text-align: left;
  border: 1px solid #ddd;
}
</style>
