<template>
  <div class="applications-page">
    <!-- Math Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 900" fill="none">
        <path d="M-100 350 C 300 150, 650 650, 1050 300 C 1280 100, 1450 450, 1650 350" stroke="rgba(229, 178, 46, 0.06)" stroke-width="1.5" />
        <path d="M-50 450 C 350 250, 750 750, 1150 400" stroke="rgba(147, 197, 253, 0.04)" stroke-width="1" />
      </svg>
    </div>

    <div class="container dashboard-container">
      <!-- Top Bar -->
      <div class="dashboard-header">
        <div class="header-left">
          <router-link to="/" class="back-link">
            <span>←</span> Bosh sahifaga qaytish
          </router-link>
          <h1 class="page-title">
            Qabullar <span class="serif-italic-gold">Boshqaruvi</span>
          </h1>
          <p class="page-subtitle">
            Olimpiadaga ro'yxatdan o'tgan o'quvchilar ro'yxati, filtrlash va Excel hisoboti.
          </p>
        </div>

        <div class="header-actions">
          <button @click="fetchData" class="btn-secondary" :disabled="loading" title="Ma'lumotlarni yangilash">
            <span :class="{ 'spin-icon': loading }">🔄</span>
            <span>Yangilash</span>
          </button>

          <button @click="exportToExcel" class="btn-editorial-pill export-btn">
            <span>📥 Excelga yuklash (.XLSX)</span>
          </button>
        </div>
      </div>

      <!-- Stats Cards -->
      <div class="stats-grid">
        <div 
          class="stat-card" 
          :class="{ active: selectedClass === '' }"
          @click="setClassFilter('')"
        >
          <div class="stat-meta">JAMI QABULLAR</div>
          <div class="stat-number font-mono">{{ stats.total || 0 }}</div>
          <div class="stat-label">Barcha arizalar</div>
        </div>

        <div 
          class="stat-card" 
          :class="{ active: selectedClass === '5' }"
          @click="setClassFilter('5')"
        >
          <div class="stat-meta">5-SINF</div>
          <div class="stat-number font-mono">{{ stats.class_5 || 0 }}</div>
          <div class="stat-label">Ishtirokchilar</div>
        </div>

        <div 
          class="stat-card" 
          :class="{ active: selectedClass === '6' }"
          @click="setClassFilter('6')"
        >
          <div class="stat-meta">6-SINF</div>
          <div class="stat-number font-mono">{{ stats.class_6 || 0 }}</div>
          <div class="stat-label">Ishtirokchilar</div>
        </div>

        <div 
          class="stat-card" 
          :class="{ active: selectedClass === '7' }"
          @click="setClassFilter('7')"
        >
          <div class="stat-meta">7-SINF</div>
          <div class="stat-number font-mono">{{ stats.class_7 || 0 }}</div>
          <div class="stat-label">Ishtirokchilar</div>
        </div>
      </div>

      <!-- Controls Row (Search & Filter) -->
      <div class="controls-card">
        <!-- Search Input -->
        <div class="search-box">
          <span class="search-icon">🔍</span>
          <input
            v-model="searchQuery"
            type="text"
            placeholder="F.I.SH. yoki telefon raqami bo'yicha qidirish..."
            class="search-input"
            @input="handleSearch"
          />
          <button v-if="searchQuery" @click="clearSearch" class="clear-search-btn">✕</button>
        </div>

        <!-- Class Filter Chips -->
        <div class="filter-chips">
          <button
            class="chip-btn"
            :class="{ active: selectedClass === '' }"
            @click="setClassFilter('')"
          >
            Barchasi ({{ stats.total || 0 }})
          </button>
          <button
            v-for="c in [5, 6, 7]"
            :key="c"
            class="chip-btn font-mono"
            :class="{ active: selectedClass === String(c) }"
            @click="setClassFilter(String(c))"
          >
            {{ c }}-sinf ({{ stats[`class_${c}`] || 0 }})
          </button>
        </div>
      </div>

      <!-- Table Section -->
      <div class="table-wrapper">
        <div class="table-header-info">
          <span class="results-count font-mono">Topildi: <strong>{{ participants.length }}</strong> ta ariza</span>
          <span v-if="searchQuery || selectedClass" class="filter-active-tag">Filter faol</span>
        </div>

        <div v-if="loading" class="table-loading">
          <div class="spinner-gold"></div>
          <p>Qabullar yuklanmoqda...</p>
        </div>

        <div v-else-if="participants.length === 0" class="table-empty">
          <div class="empty-icon">📂</div>
          <h3>Hech qanday ariza topilmadi</h3>
          <p>Qidiruv shartlarini o'zgartirib ko'ring yoki yangi arizalar kelishini kuting.</p>
        </div>

        <div v-else class="table-responsive">
          <table class="data-table">
            <thead>
              <tr>
                <th class="th-id">ID</th>
                <th class="th-name">F.I.SH. (O'QUVCHI)</th>
                <th class="th-phone">TELEFON</th>
                <th class="th-class">SINF</th>
                <th class="th-date">RO'YXATDAN O'TGAN SANA</th>
                <th class="th-actions">AMAL</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="p in participants" :key="p.id" class="table-row">
                <td class="td-id font-mono">#{{ p.id }}</td>
                <td class="td-name">
                  <span class="student-name">{{ p.full_name }}</span>
                </td>
                <td class="td-phone font-mono">
                  <a :href="`tel:${p.phone}`" class="phone-link">
                    {{ formatDisplayPhone(p.phone) }}
                  </a>
                </td>
                <td class="td-class">
                  <span class="class-badge font-mono">{{ p.class_number }}-sinf</span>
                </td>
                <td class="td-date font-mono">
                  {{ formatDate(p.created_at) }}
                </td>
                <td class="td-actions">
                  <button 
                    @click="confirmDelete(p)" 
                    class="btn-delete"
                    title="Arizani o'chirish"
                  >
                    🗑️
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Delete Confirmation Modal -->
    <transition name="modal-fade">
      <div v-if="deleteTarget" class="modal-backdrop">
        <div class="confirm-modal-card">
          <div class="modal-warn-icon">⚠️</div>
          <h3 class="modal-warn-title">Arizani o'chirishni tasdiqlaysizmi?</h3>
          <p class="modal-warn-text">
            <strong>{{ deleteTarget.full_name }}</strong> (#{{ deleteTarget.id }}) ga tegishli ma'lumot butunlay o'chiriladi.
          </p>
          <div class="modal-buttons">
            <button @click="deleteTarget = null" class="btn-cancel">Bekor qilish</button>
            <button @click="executeDelete" class="btn-confirm-delete" :disabled="deleting">
              <span v-if="deleting">O'chirilmoqda...</span>
              <span v-else>Ha, o'chirilsin</span>
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { getApplications, deleteApplication, getExportApplicationsUrl } from '../services/api.js'

const participants = ref([])
const stats = reactive({
  total: 0,
  class_5: 0,
  class_6: 0,
  class_7: 0,
})

const loading = ref(true)
const deleting = ref(false)
const searchQuery = ref('')
const selectedClass = ref('')
const deleteTarget = ref(null)
let searchTimeout = null

onMounted(() => {
  fetchData()
})

async function fetchData() {
  loading.value = true
  try {
    const data = await getApplications({
      search: searchQuery.value,
      class_number: selectedClass.value,
    })
    participants.value = data.results || []
    if (data.stats) {
      Object.assign(stats, data.stats)
    }
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

function handleSearch() {
  if (searchTimeout) clearTimeout(searchTimeout)
  searchTimeout = setTimeout(() => {
    fetchData()
  }, 350)
}

function clearSearch() {
  searchQuery.value = ''
  fetchData()
}

function setClassFilter(c) {
  selectedClass.value = c
  fetchData()
}

function formatDisplayPhone(phone) {
  if (!phone) return ''
  const p = phone.replace(/[^\d+]/g, '')
  if (p.length === 13 && p.startsWith('+998')) {
    return `${p.slice(0, 4)} ${p.slice(4, 6)} ${p.slice(6, 9)} ${p.slice(9, 11)} ${p.slice(11, 13)}`
  }
  return phone
}

function formatDate(dateStr) {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  return d.toLocaleString('uz-UZ', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

function exportToExcel() {
  const url = getExportApplicationsUrl({
    search: searchQuery.value,
    class_number: selectedClass.value,
  })
  window.open(url, '_blank')
}

function confirmDelete(p) {
  deleteTarget.value = p
}

async function executeDelete() {
  if (!deleteTarget.value) return
  deleting.value = true
  try {
    const ok = await deleteApplication(deleteTarget.value.id)
    if (ok) {
      participants.value = participants.value.filter(item => item.id !== deleteTarget.value.id)
      deleteTarget.value = null
      // Refresh stats
      fetchData()
    }
  } finally {
    deleting.value = false
  }
}
</script>

<style scoped>
.applications-page {
  min-height: 100vh;
  position: relative;
  background-color: var(--bg-deep);
  padding: calc(var(--header-height) + 30px) 0 80px;
  overflow: hidden;
}

.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 2;
}

/* Header */
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 32px;
  gap: 20px;
  flex-wrap: wrap;
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-bottom: 12px;
  transition: color 0.2s ease;
}

.back-link:hover {
  color: var(--gold);
}

.page-title {
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 6px;
  letter-spacing: -0.02em;
}

.page-subtitle {
  font-size: 0.95rem;
  color: var(--text-secondary);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  height: 46px;
  padding: 0 18px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--border-medium);
  color: #ffffff;
  font-size: 0.88rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.09);
  border-color: var(--border-light);
}

.export-btn {
  height: 46px;
  font-size: 0.9rem;
  padding: 0 22px;
  box-shadow: 0 4px 20px rgba(229, 178, 46, 0.25);
}

.spin-icon {
  display: inline-block;
  animation: spin 1s linear infinite;
}

/* Stats Cards */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}

.stat-card {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  padding: 20px 18px;
  cursor: pointer;
  transition: all 0.2s ease;
  backdrop-filter: blur(8px);
}

.stat-card:hover {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(229, 178, 46, 0.3);
  transform: translateY(-2px);
}

.stat-card.active {
  background: rgba(229, 178, 46, 0.08);
  border-color: var(--gold);
  box-shadow: 0 0 20px rgba(229, 178, 46, 0.15);
}

.stat-meta {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  margin-bottom: 8px;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1;
  margin-bottom: 6px;
}

.stat-card.active .stat-number {
  color: var(--gold);
}

.stat-label {
  font-size: 0.78rem;
  color: var(--text-secondary);
}

/* Controls */
.controls-card {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 14px;
  padding: 16px 20px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.search-box {
  position: relative;
  flex: 1;
  min-width: 280px;
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.9rem;
  opacity: 0.6;
}

.search-input {
  width: 100%;
  height: 44px;
  padding: 0 40px 0 38px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-medium);
  border-radius: 10px;
  color: #ffffff;
  font-size: 0.9rem;
  outline: none;
  transition: all 0.2s ease;
}

.search-input:focus {
  border-color: var(--gold);
  background: rgba(255, 255, 255, 0.07);
}

.clear-search-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--text-dim);
  cursor: pointer;
  font-size: 0.85rem;
}

.filter-chips {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.chip-btn {
  padding: 8px 14px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-medium);
  color: var(--text-secondary);
  font-size: 0.82rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.chip-btn:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.08);
}

.chip-btn.active {
  background: var(--gold);
  border-color: var(--gold);
  color: #070913;
  font-weight: 600;
}

/* Table Wrapper */
.table-wrapper {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 16px;
  padding: 24px;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.table-header-info {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

.filter-active-tag {
  background: rgba(229, 178, 46, 0.15);
  border: 1px solid rgba(229, 178, 46, 0.3);
  color: var(--gold);
  padding: 2px 10px;
  border-radius: 99px;
  font-size: 0.75rem;
  font-family: var(--font-mono);
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.data-table th {
  padding: 14px 16px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--text-dim);
  border-bottom: 1px solid var(--border-medium);
  background: rgba(255, 255, 255, 0.015);
}

.data-table td {
  padding: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  font-size: 0.92rem;
  vertical-align: middle;
}

.table-row:hover td {
  background: rgba(255, 255, 255, 0.025);
}

.td-id {
  font-size: 0.82rem;
  color: var(--text-dim);
}

.student-name {
  font-weight: 600;
  color: #ffffff;
}

.phone-link {
  color: var(--gold);
  text-decoration: none;
  font-size: 0.88rem;
  transition: opacity 0.2s;
}

.phone-link:hover {
  opacity: 0.8;
  text-decoration: underline;
}

.class-badge {
  display: inline-block;
  padding: 4px 10px;
  background: rgba(147, 197, 253, 0.1);
  border: 1px solid rgba(147, 197, 253, 0.25);
  color: #93c5fd;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
}

.td-date {
  font-size: 0.82rem;
  color: var(--text-secondary);
}

.btn-delete {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
  border-radius: 8px;
  padding: 6px 10px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-delete:hover {
  background: rgba(239, 68, 68, 0.25);
  border-color: #ef4444;
}

/* Loading & Empty states */
.table-loading,
.table-empty {
  padding: 60px 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  color: var(--text-secondary);
}

.empty-icon {
  font-size: 2.5rem;
}

.table-empty h3 {
  color: #ffffff;
  font-size: 1.2rem;
}

.spinner-gold {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(229, 178, 46, 0.2);
  border-top-color: var(--gold);
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

/* Modal */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(3, 4, 10, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
}

.confirm-modal-card {
  background: linear-gradient(135deg, rgba(24, 18, 40, 0.98), rgba(12, 10, 22, 0.99));
  border: 1px solid rgba(239, 68, 68, 0.3);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
  border-radius: 16px;
  padding: 32px 28px;
  max-width: 420px;
  width: 100%;
  text-align: center;
}

.modal-warn-icon {
  font-size: 2.2rem;
  margin-bottom: 12px;
}

.modal-warn-title {
  font-size: 1.2rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 8px;
}

.modal-warn-text {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 24px;
}

.modal-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.btn-cancel {
  flex: 1;
  height: 42px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid var(--border-medium);
  border-radius: 8px;
  color: #ffffff;
  font-size: 0.88rem;
  cursor: pointer;
}

.btn-confirm-delete {
  flex: 1;
  height: 42px;
  background: #ef4444;
  border: none;
  border-radius: 8px;
  color: #ffffff;
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.2s ease;
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 900px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
  .controls-card {
    flex-direction: column;
    align-items: stretch;
  }
  .table-wrapper {
    padding: 16px;
  }
}
</style>
