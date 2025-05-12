// FILEPATH: c:/Users/Kromm/Practica/hospital-react/src/layouts/AdminLayout.jsx
import React from 'react'
import { Navigate, Outlet } from 'react-router-dom'
import { useContext } from 'react'
import { UserContext } from '../context/UserContext'

function AdminLayout() {
  const { user, isAuthenticated } = useContext(UserContext)

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />
  }

  if (user?.role !== 'admin') {
    return <Navigate to="/unauthorized" replace />
  }

  return (
    <div className="admin-layout">
      {/* Add navigation components, header, etc. here */}
      <Outlet />
    </div>
  )
}

export default AdminLayout